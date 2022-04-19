from functools import wraps
from time import time
import datetime


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:{f.__name__} args:[{args}, {kw}] took: {te-ts} sec')
        return result
    return wrap

def write_to_file(text_list):
    with open(f"game_{get_time_stamp()}.log", "a+") as f:
        for tex in text_list:
            f.write(tex)

def get_time_stamp():
    t = time.time()
    return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')