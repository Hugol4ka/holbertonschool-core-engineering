#!/usr/bin/env python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        # Ce bloc s'exécute QUOI QU'IL ARRIVE
    return result
