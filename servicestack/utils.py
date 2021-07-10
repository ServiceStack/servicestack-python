import base64
import json
from datetime import datetime, timezone, timedelta
from typing import Optional


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
