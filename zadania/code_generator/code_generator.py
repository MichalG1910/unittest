from datetime import date
import random

def get_code():
    rand_int = random.randint(1,9)
    return f'CX-{rand_int}'

def get_today_name():
    return date.today().strftime('%a')              #strftime(%a) - sformatuje datę, pokaże 3 pierwsze litery dnia

def get_code_with_day():
    code = get_code()
    dayname = get_today_name().upper()
    return f'{code}-{dayname}'

