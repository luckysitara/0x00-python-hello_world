#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        answer = a / b
    except ZeroDivisionError:
        answer = none
    finally:
        print('Inside result: {}'.format(answer))
    return answer
