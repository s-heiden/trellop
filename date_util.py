import datetime
from datetime import date


def to_earliest_weekday_after(date, weekday):
    return date + datetime.timedelta(days=(weekday - date.weekday() + 7) % 7)


def to_earliest_future_weekday(weekday: str) -> str:
    weekday = to_datetime_weekday(weekday)
    result = date.today() + datetime.timedelta(days=(weekday - date.today().weekday() + 7) % 7)
    return str(result)


def to_datetime_weekday(weekday: str):
    if weekday.lower() == 'mon':
        return 0
    elif weekday.lower() == 'tue':
        return 1
    elif weekday.lower() == 'wed':
        return 2
    elif weekday.lower() == 'thu':
        return 3
    elif weekday.lower() == 'fri':
        return 4
    elif weekday.lower() == 'sat':
        return 5
    elif weekday.lower() == 'sun':
        return 6
    else:
        return -1
