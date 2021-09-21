from datetime import date, timedelta

def u_to_g(d):
    if d < date(1582, 10, 5):
        g_date = d
    elif date(1582, 10, 5) <= d < date(1700, 2, 28):
        g_date = d + 10
    elif date(1700, 3, 1) <= d < date(1800, 2, 28):
        g_date = d + 11
    elif date(1800, 3, 1) <= d < date(1900, 2, 28):
        g_date = d + 12
    elif date(1900, 3, 1) <= d < date(2100, 2, 28):
        g_date = d + timedelta(days=13)
    return g_date
