from datetime import date

def calculate_age(age):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

