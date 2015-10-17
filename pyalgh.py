

import os
import sys
import matplotlib.pyplot as pp
import time

def main():
    try:
        path = sys.argv[1]
        funcname = sys.argv[2]
    except IndexError:
        print(_usage)
        sys.exit()
    
    module = import_file(path)
    
    # I can't think of a less hacky way to do this, but still...
    func = eval("{0}.{1}".format(module.__name__,funcname))
    

def timeme(function, *args, **kwargs):
    t1 = time.perf_counter()
    function(*args, **kwargs)
    t2 = time.perf_counter()
    return t2 - t1

def import_file(parpath):
    path, filename = os.path.split(os.path.abspath(parpath))
    filename = os.path.splitext(filename)[0]
    sys.path.insert(0, path)
    module = __import__(filename)
    # Catch any horrible mangling of the user's path.
    assert sys.path.pop(0) == path, "Path being mutilated inside import_file!!"
    return module
