import base64
import json
import numbers
import os
import pathlib
import platform
import dataclasses
import typing
from datetime import datetime, timezone, timedelta
from typing import Optional, List, Dict, Any, Type, get_origin, Union, get_args
from dataclasses import dataclass, field, asdict
from functools import reduce
from .log import Log


def is_optional(cls: Type): return get_origin(cls) is Union and type(None) in get_args(cls)


def is_list(cls: Type): return cls == typing.List or cls == list or get_origin(cls) == list


def is_dict(cls: Type): return cls == typing.Dict or cls == dict or get_origin(cls) == dict


def generic_args(cls: Type):
    if not hasattr(cls, '__args__'):
        raise TypeError(f"{cls} is not a Generic Type")
    return cls.__args__


def generic_arg(cls: Type): return generic_args(cls)[0]


def index_of(target: str, needle: str):
    try:
        return target.index(needle)
    except ValueError:
        return -1


def last_index_of(target: str, needle: str):
    try:
        return target.rindex(needle)
    except ValueError:
        return -1


def left_part(str_val: Optional[str], needle: str):
    if str_val is None:
        return None
    pos = index_of(str_val, needle)
    return str_val if pos == -1 else str_val[:pos]


def right_part(str_val: Optional[str], needle: str):
    if str_val is None:
        return None
    pos = index_of(str_val, needle)
    return str_val if pos == -1 else str_val[pos + len(needle):]


def last_left_part(str_val: Optional[str], needle: str):
    if str_val is None:
        return None
    pos = last_index_of(str_val, needle)
    return str_val if pos == -1 else str_val[:pos]


def last_right_part(str_val: Optional[str], needle: str):
    if str_val is None:
        return None
    pos = last_index_of(str_val, needle)
    return str_val if pos == -1 else str_val[pos + len(needle):]


def split_on_first(s: Optional[str], c: str):
    if str is None or str == "":
        return [s]
    pos = index_of(s, c)
    if pos >= 0:
        return [s[:pos], s[pos + 1:]]
    return [s]


def split_on_last(s: Optional[str], c: str):
    if str is None or str == "":
        return [s]
    pos = last_index_of(s, c)
    if pos >= 0:
        return [s[:pos], s[pos + 1:]]
    return [s]


def to_timespan(duration: timedelta):
    total_seconds = duration.total_seconds()
    whole_seconds = total_seconds // 1
    seconds = whole_seconds
    sec = int(seconds % 60 if seconds >= 60 else seconds)
    seconds = seconds // 60
    min = int(seconds % 60)
    seconds = seconds // 60
    hours = int(seconds % 60)
    days = seconds // 24
    remaining_secs = float(sec + (total_seconds - whole_seconds))

    sb = ["P"]
    if days > 0:
        sb.append(f"{days}D")

    if days == 0 or hours + min + sec + remaining_secs > 0:
        sb.append("T")
        if hours > 0:
            sb.append(f"{hours}H")
        if min > 0:
            sb.append(f"{min}M")

        if remaining_secs > 0:
            sec_fmt = "{:.7f}".format(remaining_secs)
            sec_fmt = sec_fmt.rstrip('0')
            sec_fmt = sec_fmt.rstrip('.')
            sb.append(sec_fmt)
            sb.append("S")
        elif len(sb) == 2:  # PT
            sb.append("0S")

    xsd = ''.join(sb)
    # print(f"XSD: {xsd}, {days}:{hours}:{min}:{remaining_secs}")
    return xsd


def from_timespan(s: Optional[str]):
    if s is None:
        return None
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    ms = 0.0

    if s[0] != "P":
        raise ValueError(f"{s} is not a valid XSD Duration")

    s = s[1:]  # strip P
    t = split_on_first(s, 'T')
    has_time = len(t) == 2

    d = split_on_first(t[0], 'D')
    if len(d) == 2:
        days = int(d[0])

    if has_time:
        h = split_on_first(t[1], 'H')
        if len(h) == 2:
            hours = int(h[0])

        m = split_on_first(h[len(h) - 1], 'M')
        if len(m) == 2:
            minutes = int(m[0])

        s = split_on_first(m[len(m) - 1], 'S')
        if len(s) == 2:
            ms = float(s[0])

        seconds = int(ms)
        ms -= seconds

    # print(f"\n\ntimedelta({str})[{has_time}] = {hours}:{minutes}:{seconds}\n\n")
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, milliseconds=int(ms * 1000))


_MIN_UTC_DATE = datetime.min.replace(tzinfo=timezone.utc)
_MIN_EPOCH = _MIN_UTC_DATE.timestamp()
_MAX_UTC_DATE = datetime.max.replace(tzinfo=timezone.utc)


def to_datetime(date: datetime):
    try:
        return f"/Date({int(date.timestamp() * 1000)})/"
    except Exception as e:
        Log.debug(f"to_datetime({date}): e")
        return None


def from_datetime(json_date: str):
    if json_date.startswith("/Date("):
        epoch_and_zone = left_part(right_part(json_date, "("), ")")
        epoch_str = epoch_and_zone
        if index_of(epoch_and_zone[1:], '-') >= 0:
            epoch_str = last_left_part(epoch_and_zone, '-')
        if index_of(epoch_and_zone[1:], '+') >= 0:
            epoch_str = last_left_part(epoch_and_zone, '+')
        epoch = int(epoch_str)
        try:
            return datetime.fromtimestamp(epoch / 1000, timezone.utc)
        except Exception as e:
            if epoch < _MIN_EPOCH:
                return _MIN_UTC_DATE
            else:
                return _MAX_UTC_DATE

    # need to reduce to 6f precision and remove trailing Z
    has_sec_fraction = index_of(json_date, '.') >= 0
    is_utc = json_date.endswith('Z')
    if is_utc:
        json_date = json_date[0:-1]
    if has_sec_fraction:
        sec_fraction = last_right_part(json_date, '.')
        tz = ''
        if '+' in sec_fraction:
            tz = '+' + right_part(sec_fraction, '+')
            sec_fraction = left_part(sec_fraction, '+')
        elif '-' in sec_fraction:
            sec_fraction = left_part(sec_fraction, '-')
        if len(sec_fraction) > 6:
            json_date = last_left_part(json_date, '.') + '.' + sec_fraction[0:6] + tz

    if is_utc:
        return datetime.fromisoformat(json_date).replace(tzinfo=timezone.utc)
    else:
        return datetime.fromisoformat(json_date)


def to_bytearray(value: Optional[bytes]):
    if value is None:
        return None
    return base64.b64encode(value).decode('ascii')


def from_bytearray(base64str: Optional[str]):
    return base64.b64decode(base64str)


def from_base64url_safe(input_str: str):
    output = input_str
    output = output.replace('-', '+')
    output = output.replace('_', '/')
    pad = len(output) % 4
    if pad == 2:
        output += "=="
    elif pad == 3:
        output += "="
    elif pad != 0:
        raise ValueError("Illegal base46url string!")
    return base64.b64decode(output)


def _decode_base64url_payload(payload: str):
    payload_bytes = from_base64url_safe(payload)
    payload_json = payload_bytes.decode('utf-8')
    return json.loads(payload_json)


def inspect_jwt(jwt: str):
    head = _decode_base64url_payload(left_part(jwt, '.'))
    body = _decode_base64url_payload(left_part(right_part(jwt, '.'), '.'))
    exp = int(body['exp'])
    return head, body, datetime.fromtimestamp(exp, timezone.utc)


# inspect utils
def _asdict(obj):
    if isinstance(obj, dict):
        return obj
    elif dataclasses.is_dataclass(obj):
        return asdict(obj)
    elif hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return obj


def _asdicts(obj):
    t = type(obj)
    if is_list(t):
        to = []
        for o in obj:
            to.append(_asdicts(o))
        return to
    elif is_dict(t):
        to = {}
        for k in obj:
            to[k] = _asdicts(obj[k])
        return to
    else:
        return _asdict(obj)


def _allkeys(obj):
    keys = []
    for o in obj:
        for key in o:
            if not key in keys:
                keys.append(key)
    return keys


def inspect_vars(objs):
    if not isinstance(objs, dict):
        raise TypeError('objs must be a dictionary')

    to = _asdicts(objs)

    inspect_vars_path = os.environ.get('INSPECT_VARS')
    if inspect_vars_path is None:
        return
    if platform.system() == 'Windows':
        inspect_vars_path = inspect_vars_path.replace("/", "\\")
    else:
        inspect_vars_path = inspect_vars_path.replace("\\", "/")

    pathlib.Path(os.path.dirname(inspect_vars_path)).mkdir(parents=True, exist_ok=True)

    with open(inspect_vars_path, 'w') as outfile:
        json.dump(to, outfile)


def dump(obj):
    print(_asdicts(obj))
    return json.dumps(_asdicts(obj), indent=4).replace('"', '').replace(': null', ':')


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
    half = (length // 2 - nlen // 2)
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
    s = f"{obj}"
    if len(s) <= length:
        if isinstance(obj, numbers.Number):
            return _align_right(s, length, pad)
        return _align_left(s, length, pad)
    return s


def dumptable(objs, headers=None):
    if not is_list(type(objs)):
        raise TypeError('objs must be a list')
    map_rows = _asdicts(objs)
    if headers is None:
        headers = _allkeys(map_rows)
    col_sizes: Dict[str, int] = {}

    for k in headers:
        max = len(k)
        for row in map_rows:
            if k in row:
                col = row[k]
                val_size = len(f"{col}")
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
            to += '' + _align_auto(row[k], col_sizes[k]) + "|"
        sb.append(to)

    sb.append(f"+{'-' * (row_width - 2)}+")
    return '\n'.join(sb)


def printdumptable(obj, headers=None):
    print(dumptable(obj, headers))
