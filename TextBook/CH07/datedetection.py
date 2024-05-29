import re


def is_valid_date(date_str):
    date_pattern = r'^(0?[1-9]|[1-2][0-9]|3[0-1])/(0?[1-9]|1[0-2])/((19|20)\d{2})$'

    
    if not re.match(date_pattern, date_str):
        return False

    day, month, year = map(int, date_str.split('/'))

    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False

    return True



date_str = '29/02/2024'
if is_valid_date(date_str):
    print(f'{date_str}は有効な日付です。')
else:
    print(f'{date_str}は無効な日付です。')