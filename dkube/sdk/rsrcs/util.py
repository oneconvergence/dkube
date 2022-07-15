import string
import random

generate = lambda hint: "{}-{}".format(hint, ''.join(random.sample(string.ascii_letters + string.digits, 6)))

def list_of_strs(x):
    if x != None:
        if type(x) == list:
            #make sure each element is of type str
            x = [str(y) for y in x]
        else:
            x = [str(x)]
    return x
