from datetime import datetime

def is_leap(year):
    if year < 1918:
        return year % 4 == 0  # Julian calendar
    elif year > 1918:
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)  # Gregorian calendar
    else:
        return False  # 1918 is a special case


def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    elif is_leap(year):
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"


