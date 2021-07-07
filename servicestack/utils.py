from datetime import timedelta

def to_timespan(duration:timedelta):
    total_seconds = duration.total_seconds()
    whole_seconds = total_seconds // 1
    seconds = whole_seconds
    sec = seconds % 60 if seconds >= 60 else seconds
    seconds = seconds // 60
    min = seconds % 60
    seconds = seconds // 60
    hours = seconds % 60
    days = seconds // 24
    remaining_secs = float(sec + (total_seconds - whole_seconds))

    sb=["P"]
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
        elif sb.count == 2: #PT
            sb.append("0S")

    xsd = ''.join(sb)
    return xsd
