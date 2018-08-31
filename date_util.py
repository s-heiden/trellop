"""Provided utilities in regard to dates"""
import datetime
from datetime import date


def to_earliest_weekday_after(src_date, weekday):
    """Return the date of earliest given weekday after given source date in datetime format"""
    return src_date + datetime.timedelta(days=(weekday - src_date.weekday() + 7) % 7)


def to_earliest_future_weekday(weekday: str) -> str:
    """Return the date of earliest given weekday after now"""
    weekday = to_datetime_weekday(weekday)
    result = to_earliest_weekday_after(date.today(), weekday)
    return str(result)


def to_datetime_weekday(weekday: str):
    """Return the number corresponding to weekday string in datetime format"""
    res = -1

    if weekday.lower() == 'mon':
        res = 0
    if weekday.lower() == 'tue':
        res = 1
    if weekday.lower() == 'wed':
        res = 2
    if weekday.lower() == 'thu':
        res = 3
    if weekday.lower() == 'fri':
        res = 4
    if weekday.lower() == 'sat':
        res = 5
    if weekday.lower() == 'sun':
        res = 6

    return res
