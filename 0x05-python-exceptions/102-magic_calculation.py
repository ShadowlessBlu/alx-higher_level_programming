#!/usr/bin/python3
def magic_calculation(a, b):
    info = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            info += a ** b / i
        except Exception:
            info = b + a
            break
    return info
