import string
import random

generate = lambda hint: "{}-{}".format(hint, ''.join([random.choice(string.digits) for n in range(4)]))

def choices(*args):
    return args[0]

def validate_choices(value, *args):
    return value in args[0]
