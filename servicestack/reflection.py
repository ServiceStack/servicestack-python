import base64
import collections.abc as collections
import decimal
import inspect
import json
import math
import numbers
import os
import pathlib
import platform
import typing
import sys
import uuid
from dataclasses import fields, is_dataclass
from datetime import datetime, timedelta, date, time
from enum import Enum, IntEnum, EnumMeta
from functools import reduce
from types import MappingProxyType
from typing_extensions import Type, get_origin, get_args
from typing import Callable, ForwardRef, Union, TypeVar
from typing import List, Dict, Any

import marshmallow.fields as mf

from servicestack.log import Log
from servicestack.utils import to_timespan, to_datetime, to_bytearray, from_bytearray, from_datetime, from_timespan
from .utils import clean_camelcase, snakecase, uppercase, camelcase


def is_optional(cls: Type): return get_origin(cls) is Union and type(None) in get_args(cls)


def is_list(cls: Type): return cls == typing.List or cls == list or get_origin(cls) == list


def is_dict(cls: Type): return cls == typing.Dict or cls == dict or get_origin(cls) == dict or cls == MappingProxyType


def nameof(instance):
    return type(instance).__name__


def generic_args(cls: Type):
    if not hasattr(cls, '__args__'):
        raise TypeError(f"{cls} is not a Generic Type")
    return cls.__args__


def generic_arg(cls: Type): return generic_args(cls)[0]


def _get_type_vars_map(cls: Type, type_map=None):
    if type_map is None:
        type_map = {}
    if hasattr(cls, '__orig_bases__'):
        for base_cls in cls.__orig_bases__:
            _get_type_vars_map(base_cls, type_map)
    generic_def = get_origin(cls)
    if generic_def is not None:
        generic_type_args = get_args(cls)
        i = 0
        for t in generic_def.__parameters__:
            k = t
            if type(k) == TypeVar:
                k = k.__name__
            type_map[k] = generic_type_args[i]
            i += 1
    return type_map


def _dict_with_string_keys(d: dict):
    to = {}
    for k, v in d.items():
        to[f"{k}"] = v
    return to


def has_type_vars(cls: Type):
    if cls is None:
        return None
    return isinstance(cls, TypeVar) or any(isinstance(x, TypeVar) for x in cls.__args__)


def _empty(x):
    return x is None or x == {} or x == []


def _str(x: Any):
    if type(x) == str:
        return x
    return f"{x}"


def identity(x: Any): return x


_JSON_TYPES = {str, bool, int, float}
_BUILT_IN_TYPES = {
    str, bool, int, float, decimal.Decimal, datetime, timedelta, date, time, uuid.UUID,
    bytes, bytearray, complex,    
}

def is_builtin(t: Type):
    try:
        return t in _BUILT_IN_TYPES or issubclass(t, Enum)
    except Exception:  # throws if t is not hashable
        return False


def to_dict(obj: Any, key_case: Callable[[str], str] = identity, remove_empty: bool = True):
    t = type(obj)
    if obj is None or is_builtin(t):
        return obj
    if is_list(t):
        to = []
        for o in obj:
            use_val = to_dict(o, key_case=key_case, remove_empty=remove_empty)
            if not remove_empty or use_val is not None:
                to.append(use_val)
    elif is_dict(t):
        to = {}
        for k, v in obj.items():
            use_key = key_case(_str(k))
            use_val = to_dict(v, key_case=key_case, remove_empty=remove_empty)
            if not remove_empty or use_val is not None:
                to[use_key] = use_val
    elif hasattr(obj, 'to_dict'):  # dataclass
        d = obj.to_dict()
        to = {}
        for k, v in d.items():
            use_key = key_case(_str(k))
            use_val = to_dict(v, key_case=key_case, remove_empty=remove_empty)
            if not remove_empty or use_val is not None:
                to[use_key] = use_val
    elif hasattr(obj, '__dict__'):
        to = to_dict(vars(obj), key_case=key_case, remove_empty=remove_empty)
    else:
        to = obj
    if remove_empty:
        return clean_any(to)
    return to


def _clean_list(d: list):
    return [v for v in (clean_any(v) for v in d) if not _empty(v)]


def _clean_dict(d: dict):
    return {k: v for k, v in ((k, clean_any(v)) for k, v in d.items()) if not _empty(v)}


def clean_any(d):
    """recursively remove empty lists, empty dicts, or None elements from a dictionary"""
    if is_dict(d):
        return _clean_dict(d)
    elif is_list(d):
        return _clean_list(d)
    else:
        return d


def _json_encoder(obj: Any):
    t = type(obj)
    if is_dataclass(t) or is_dict(t):
        return to_dict(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, timedelta):
        return to_timespan(obj)
    if isinstance(obj, bytes):
        return base64.b64encode(obj).decode('ascii')
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    if t in _JSON_TYPES:
        return obj
    if is_builtin(t):
        return _str(obj)
    raise TypeError(f"Unsupported Type in JSON encoding: {t}")


def to_json(obj: Any, indent=None, compact=False):
    if compact:
        return json.dumps(to_dict(obj), separators=(',', ':'), default=_json_encoder)
    else:
        return json.dumps(to_dict(obj), indent=indent, default=_json_encoder)

def to_jsv_data(request: Any):
    """
    Convert request DTO to dict of (key, value) tuples for request session .data arg
    """
    request_dict = to_dict(request)
    request_tuples = []
    for k, v in request_dict.items():
        if is_builtin(type(v)):
            request_tuples.append((k, _json_encoder(v)))
        else:
            request_tuples.append((k, to_json(v, compact=True)))
    return request_tuples

class TypeConverters:
    serializers = {}    # Py3.9: dict[Type, Callable[[Any], Any]]
    deserializers = {}  # Py3.9: dict[Type, Callable[[Any], Any]]

    @staticmethod
    def register(cls: Type, serializer: Callable[[Any], Any] = None, deserializer: Callable[[Any], Any] = None):
        if serializer is not None:
            TypeConverters.serializers[cls] = serializer
        if deserializer is not None:
            TypeConverters.deserializers[cls] = deserializer

    @staticmethod
    def serialize(obj: Any):
        cls = type(obj)
        if cls in TypeConverters.serializers:
            serializer = TypeConverters.serializers[cls]
            try:
                return serializer(obj)
            except Exception as e:
                Log.error(f"serializer(obj) {cls}({obj})", e)
                raise e

    @staticmethod
    def deserialize(cls: Type, obj: Any):
        deserializer = TypeConverters.deserializers[cls]
        try:
            return deserializer(obj)
        except Exception as e:
            Log.error(f"deserializer(obj) {cls}({obj})", e)
            raise e


TypeConverters.serializers = {
    datetime: to_datetime,
    timedelta: to_timespan,
    bytes: to_bytearray,
    bytearray: to_bytearray,
}
TypeConverters.deserializers = {
    mf.DateTime: from_datetime,
    mf.TimeDelta: from_timespan,
    datetime: from_datetime,
    timedelta: from_timespan,
    bytes: from_bytearray,
    bytearray: from_bytearray,
}


def _resolve_forwardref(cls: Type, orig: Type = None):
    type_name = cls.__forward_arg__
    if orig is not None and orig.__name__ == type_name:
        return orig
    if type_name not in globals():
        raise TypeError(f"Could not resolve ForwardRef('{type_name}')")
    return globals()[type_name]


def unwrap(cls: Type, module:str):
    if type(cls) == ForwardRef:
        cls = _resolve_forwardref(cls)
    if isinstance(cls, str):
        cls = eval(cls, {}, vars(sys.modules[module]))
    if is_optional(cls):
        return generic_arg(cls)
    return cls


def dict_get(name: str, obj: dict, case: Callable[[str], str] = None):
    if name in obj:
        return obj[name]
    if case:
        name_case = case(name)
        if name_case in obj:
            return obj[name_case]
    name_snake = snakecase(name)
    if name_snake in obj:
        return obj[name_snake]
    name_camel = camelcase(name)
    if name_camel in obj:
        return obj[name_camel]
    if name.endswith('_'):
        return dict_get(name.rstrip('_'), obj, case)
    return None


def sanitize_name(s: str):
    return s.replace('_', '').upper()


def enum_get(cls: Union[Enum, Type], key: Union[str, int]):
    if type(key) == int or issubclass(cls, IntEnum):
        return cls(key)
    try:
        return cls[key]
    except Exception as e:
        try:
            upper_snake = uppercase(snakecase(key))
            return cls[upper_snake]
        except Exception as e2:
            sanitize_key = sanitize_name(key)
            for value in cls.__members__.values():
                if sanitize_key == sanitize_name(value):
                    return value
            for member in cls.__members__.keys():
                if sanitize_key == sanitize_name(member):
                    return cls[member]
    raise TypeError(f"{key} is not a member of {nameof(Enum)}")


def _resolve_type(cls: Type, substitute_types: Dict[Type, type] ):
    if type(cls) == TypeVar:
        # TypeVar('T') == TypeVar('T') is false, 
        # I think this should work
        cls = cls.__name__
    if substitute_types is None:
        return cls
    return substitute_types[cls] if cls in substitute_types else cls


def convert(into: Type, obj: Any, substitute_types: Dict[Type, type] = None, module = None):
    if obj is None:
        return None
    into = unwrap(into, module)
    into = _resolve_type(into, substitute_types)
    if Log.debug_enabled():
        Log.debug(f"convert({into}, {substitute_types}, {obj})")

    is_type = type(into) == type
    if not is_type:
        Log.debug(f"type of {into} is not a class")

    generic_def = get_origin(into)
    if generic_def is not None and is_dataclass(generic_def):
        reified_types = _get_type_vars_map(into)
        return convert(generic_def, obj, reified_types)

    if is_dataclass(into):
        to = {}
        for f in fields(into):
            val = dict_get(f.name, obj)
            # print(f"to[{f.name}] = convert({f.type}, {val}, {substitute_types})")
            to[f.name] = convert(f.type, val, substitute_types, into.__module__)
            # print(f"to[{f.name}] = {to[f.name]}")
        return into(**to)
    elif is_list(into):
        el_type = _resolve_type(generic_arg(into), substitute_types)
        to = []
        for item in obj:
            to.append(convert(el_type, item, substitute_types, into.__module__))
        return to
    elif is_dict(into):
        key_type, val_type = generic_args(into)
        key_type = _resolve_type(key_type, substitute_types)
        val_type = _resolve_type(val_type, substitute_types)
        to = {}
        if not hasattr(obj, 'items'):
            Log.warn(f"dict {obj} ({type(type)}) does not have items()")
        for key, val in obj.items():
            to_key = convert(key_type, key, substitute_types, into.__module__)
            to_val = convert(val_type, val, substitute_types, into.__module__)
            to[to_key] = to_val
        return to
    else:
        if into in TypeConverters.deserializers:
            converter = TypeConverters.deserializers[into]
            try:
                return converter(obj)
            except Exception as e:
                Log.error(f"converter(obj) {into}({obj})", e)
                raise e
        elif inspect.isclass(into) and issubclass(into, mf.Field):
            try:
                return into().deserialize(obj)
            except Exception as e:
                Log.error(f"into().deserialize(obj) {into}({obj})", e)
                raise e
        elif is_type and (issubclass(into, Enum) or into == EnumMeta):
            try:
                return enum_get(into, obj)
            except Exception as e:
                print(into, type(into), obj, type(obj))
                Log.error(f"Enum into[obj] {into}[{obj}]", e)
                raise e
        else:
            try:
                return into(obj)
            except Exception as e:
                # if into == typing.Dict or get_origin(into) == typing.Dict:
                #     print("WAS A typing.Dict")
                Log.error(f"into(obj) {into}({obj})", e)
                raise e


def from_json(into: Type, json_str: str):
    if json_str is None or json_str == "":
        return None
    json_obj = json.loads(json_str)
    return convert(into, json_obj)


# inspect utils
def all_keys(obj):
    keys = []
    if not isinstance(obj, collections.Iterable):
        return keys
    for o in obj:
        if is_builtin(type(o)):
            continue
        for key in o:
            key = _str(key)
            if key is not None and key not in keys:
                keys.append(key)
    return keys


def inspect_vars(objs):
    if not isinstance(objs, dict):
        raise TypeError('objs must be a dictionary')

    to = to_dict(objs)

    inspect_vars_path = os.environ.get('INSPECT_VARS')
    if inspect_vars_path is None:
        return
    if platform.system() == 'Windows':
        inspect_vars_path = inspect_vars_path.replace("/", "\\")
    else:
        inspect_vars_path = inspect_vars_path.replace("\\", "/")

    pathlib.Path(os.path.dirname(inspect_vars_path)).mkdir(parents=True, exist_ok=True)

    with open(inspect_vars_path, 'w') as outfile:
        json_str = to_json(to)
        outfile.write(json_str)


def dump(obj):
    return to_json(obj, indent=4).replace('"', '').replace(': null', ':')


def printdump(obj):
    print(dump(obj))


def _align_left(s: str, length: int, pad: str = ' '):
    if length < 0:
        return ""
    alen = length + 1 - len(s)
    if alen <= 0:
        return s
    return pad + s + (pad * (length + 1 - len(s)))


def _align_center(s: str, length: int, pad: str = ' '):
    if length < 0:
        return ""
    nlen = len(s)
    half = math.floor(length / 2 - nlen / 2)
    odds = abs((nlen % 2) - (length % 2))
    return (pad * (half + 1)) + s + (pad * (half + 1 + odds))


def _align_right(s: str, length: int, pad: str = ' '):
    if length < 0:
        return ""
    alen = length + 1 - len(s)
    if alen <= 0:
        return s
    return (pad * (length + 1 - len(s))) + s + pad


def _align_auto(obj: Any, length: int, pad: str = ' '):
    s = _str(obj)
    if len(s) <= length:
        if isinstance(obj, numbers.Number):
            return _align_right(s, length, pad)
        return _align_left(s, length, pad)
    return s


def sanitize_key(key: str): return key.replace("_", " ").replace(" ", "").lower()


def lenient_getitem(obj: dict, key: str):
    if key in obj:
        return obj[key]
    sanitized_key = sanitize_key(key)
    for k in obj:
        if sanitize_key(k) == sanitized_key:
            return obj[k]
    return ""


def table(objs, headers=None):
    if not is_list(type(objs)):
        raise TypeError('objs must be a list')
    map_rows = to_dict(objs)
    if headers is None:
        headers = all_keys(map_rows)
    col_sizes: Dict[str, int] = {}

    for k in headers:
        max = len(k)
        for row in map_rows:
            col = lenient_getitem(row, k)
            if col != "":
                val_size = len(_str(col))
                if val_size > max:
                    max = val_size
            col_sizes[k] = max

    # sum + ' padding ' + |
    row_width = reduce(lambda x, y: x + y, col_sizes.values(), 0) + \
                (len(col_sizes) * 2) + \
                (len(col_sizes) + 1)
    sb: List[str] = [f"+{'-' * (row_width - 2)}+"]
    head = "|"
    for k in headers:
        head += _align_center(k, col_sizes[k]) + "|"
    sb.append(head)
    sb.append(f"|{'-' * (row_width - 2)}|")

    for row in map_rows:
        to = "|"
        for k in headers:
            to += '' + _align_auto(lenient_getitem(row, k), col_sizes[k]) + "|"
        sb.append(to)

    sb.append(f"+{'-' * (row_width - 2)}+")
    return '\n'.join(sb)


def printtable(obj, headers=None):
    print(table(obj, headers))


def htmllist(d: dict):
    sb: List[str] = ["<table><tbody>"]
    for k, v in d.items():
        sb.append(f"<tr><th>{_str(k)}</th><td>{htmldump(v)}</td></tr>")
    sb.append("</tbody></table>")
    return ''.join(sb)


def htmldump(objs, headers=None):
    if is_builtin(type(objs)):
        return _str(objs)

    map_rows = to_dict(objs)
    t = type(map_rows)
    if is_dict(t):
        return htmllist(map_rows)

    if headers is None:
        headers = all_keys(map_rows)

    # print(headers, map_rows)

    sb: List[str] = ["<table>"]
    row = ["<thead><tr>"]
    for k in headers:
        row.append(f"<th>{k}</th>")
    row.append("</tr></head>")
    if len(row) > 2:
        sb.append(''.join(row))
    sb.append("<tbody>")

    rows = []
    for item in map_rows:
        rows.append("<tr>")
        if len(headers) > 0:
            row = []
            for k in headers:
                val = lenient_getitem(item, k)
                row.append(f"<td>{htmldump(val)}</td>")
            rows.append(''.join(row))
        else:
            rows.append(f"<td>{htmldump(item)}</td>")
        rows.append("</tr>")

    sb.append(''.join(rows))
    sb.append("</tbody>")
    sb.append("</table>")
    return '\n'.join(sb)


def printhtmldump(obj, headers=None):
    print(htmldump(obj, headers))
