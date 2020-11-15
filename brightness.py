def get_bright(hour):
    if hour == 0:
        return 16
    elif hour == 1 or hour == 23:
        return 16
    elif hour == 2 or hour == 22:
        return 18
    elif hour == 3 or hour == 21:
        return 18
    elif hour == 4 or hour == 20:
        return 20
    elif hour == 5 or hour == 19:
        return 22
    elif hour == 6 or hour == 18:
        return 24
    elif hour == 7 or hour == 17:
        return 32
    elif hour == 8 or hour == 16:
        return 64
    elif hour == 9 or hour == 15:
        return 82
    elif hour == 10 or hour == 14:
        return 96
    elif hour == 11 or hour == 13:
        return 108
    elif hour == 12:
        return 128