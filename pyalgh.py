#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pyalgh.py / The Python Algorithm Helper
# Algorithm design tool for Python. Uses matplotlib to graph
# your function's run time on different inputs.
#
# Copyright ©2015 Benjamin Kulas.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import matplotlib.pyplot as pp
import numpy as np
from time import perf_counter
import random

def main():
    try:
        path = sys.argv[1]
        funcname = sys.argv[2]
        argspath = sys.argv[3]
    except IndexError:
        print(_usage)
        sys.exit()
    
    try:
        module = import_file(path)
    except ImportError:
        print(_module_not_found % path)
        sys.exit()
    
    # This is pretty hacky, but there's no better solution..?
    func = eval("{0}.{1}".format(module.__name__,funcname))
    
    try:
        with open(argspath) as argfile:
            rigor, start, stop, step, expr, kwargs = read_args(argfile)
    except FileNotFoundError:
        print(_args_not_found % argspath)
        sys.exit()
    
    x = []
    y = []
    for n in range(start, stop, step):
        timing = []
        for i in range(rigor):
            timings += timeme(func, *eval(expr), **kwargs)
        x.append(n)
        y.append(sum(timings) / rigor)
    
    pp.plot(x, y)
    pp.xlabel('n')
    pp.ylabel('Time Taken')
    pp.show()        

def timeme(function, *args, **kwargs):
    t1 = perf_counter()
    function(*args, **kwargs)
    t2 = perf_counter()
    return t2 - t1

def import_file(parpath):
    path, filename = os.path.split(os.path.abspath(parpath))
    filename = os.path.splitext(filename)[0]
    sys.path.insert(0, path)
    module = __import__(filename)
    # Catch any horrible mangling of the user's path.
    assert sys.path.pop(0) == path, "Path being mutilated inside import_file!"
    return module

def read_args(file):
    kwargs = {}
    text = [line.strip() for line in file.readlines()]
    rigor = int(text[0])
    if text[1].count(':') == 2:
        start, stop, step = map(int,text[1].split(':'))
    else:
        start, stop = map(int,text[1].split(':'))
        step = 1
    expr = text[2].replace('?', 'n')
    for line in text[3:]:
        key, value = line.split('=')
        kwargs[key] = value
    return rigor, start, stop, step, expr, kwargs

_usage = "Usage: pyalgh (path-to-module) (function-name) (path-to-argfile)"
_module_not_found = "Error: Could not find Python module %s"
_args_not_found= "Error: Could not find argfile %s"

main()
