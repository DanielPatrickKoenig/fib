def fib(x):
    n = 1
    ln = 1
    i = 0
    while(i < x):
        i+=1
        ln = n + ln
        n = ln - n
    return n

# code below will give you first 300 numbers in the sequence.

# import numpy as np
# return [fib(n) for n in np.arange(0,300)]

        