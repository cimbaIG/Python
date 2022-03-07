import numpy as np

def nextpow2(args):
    """ P = nextpow2(A) returns the exponents 
    for the smallest powers of two that satisfy 2^n >= abs(A)
    for each element in A. You can use nextpow2 to pad the signal 
    you pass to fft. Doing so can speed up the computation of the 
    FFT when the signal length is not an exact power of 2. 
    Function is written and tested according to Matlab tutorials.
    https://www.mathworks.com/help/matlab/ref/nextpow2.html """
    i = 0
    ar = np.zeros(len(args))
    for val in args:
        val = abs(val)
        n = 0
        if 2**n >= val:
            val = n
            ar[i] = val
        else:
            while 2**n < val:
                n += 1
            val = n
            ar[i] = val
        i += 1
    return ar

#Testing nextpow2 function
a = np.array([1, -2, 3, -4, 5, 9, 519])
print(nextpow2(a))