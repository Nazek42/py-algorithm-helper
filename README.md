# py-algorithm-helper
Algorithm design tool for Python. Uses matplotlib to graph your function's run time on different inputs.

<h3> Argfile Syntax</h3>

    smoothing
    start:stop[:step]
    args
    [kwarg=value]
    [kwarg2=value2]
    
`smoothing`: Number of times to take each data point. A higher number will result in a smoother curve, but the test will take longer.

`start:stop[:step]`: Arguments to a range() function. step defaults to 1 if not specified.

`args`: A valid Python list consisting of the arguments to your function. Any `N` in this line will be replaced with every number in the above range in turn. While writing this line, you may assume that the `random` module has been imported, therefore something like `[random.random()]` to pass your function a random float is perfectly valid.

If your function requires any keyword arguments, place them after the first three lines, one per line.

<h5>Fun with the arguments line</h5>
You can do some interesting things using only expressions. For example, if you are testing a sort algorithm, you may want a random list. This arg-line gives a random list of proportional size with items of proportional size:

    [[random.randint(1, N) for i in range(N)]]

Note the double brackets so as to pass an actual list to the function.

Or, if you have a hashing algorithm and you want to test it on ASCII strings:

    [map(chr, [random.choice(32, 127) for i in range(N)])]

The possiblities are endless.
