import string
import random

generate = lambda hint: "{}-{}".format(hint, ''.join([random.choice(string.digits) for n in range(4)]))
