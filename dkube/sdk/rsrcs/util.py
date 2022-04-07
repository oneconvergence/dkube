import string
import random
from datetime import datetime

def generate(prefix):
    random.seed(datetime.now())
    # truncate length of the prefix to 12 characters
    prefix = prefix[:12]
    #Total length = 16 characters
    N = 16
    #length of random characters to be generated
    random_len = N - len(prefix) - 1
    return "{}-{}".format(prefix, ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase +
                             string.digits) for n in range(random_len)]))

def list_of_strs(x):
    if x != None:
        if type(x) == list:
            #make sure each element is of type str
            x = [str(y) for y in x]
        else:
            x = [str(x)]
    return x
