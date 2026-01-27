from datetime import datetime, timezone

def odd_or_even_day(timestamp):
    day = datetime.fromtimestamp(timestamp/1000, timezone.utc).strftime('%d')
    return "even" if int(day) % 2 == 0 else "odd"