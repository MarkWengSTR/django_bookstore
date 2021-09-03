def time_in_range(start, end, req):
    if start <= end:
        return start <= req <= end
    else:
        return start <= req or req <= end


def add_12_afternoon(hour, noon="am"):
    return str(int(hour) + 12) if noon.strip() == "pm" else hour
