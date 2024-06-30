from datetime import datetime

def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    delta = today - date

    return delta.days

print(get_days_from_today("2024-5-30"))