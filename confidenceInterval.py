import re
import sys
import math
from scipy.stats import sem, t
from scipy import mean

import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

filename1 = sys.argv[1]
filename2 = sys.argv[2]
skip = 22
if len(sys.argv) > 3 :
    skip += int(sys.argv[3])

pad1 = np.loadtxt(filename1, dtype='float', delimiter='\t', usecols=(0), unpack=True, skiprows=skip)
pad2 = np.loadtxt(filename2, dtype='float', delimiter='\t', usecols=(0), unpack=True, skiprows=skip)


if len(pad1) > len(pad2):
    pad1 = pad1[:len(pad2)]
elif len(pad2) > len(pad1):
    pad2 = pad2[:len(pad1)]

#errors = pad1 - pad2

confidence = 0.95
n = len(pad2)
m = mean(pad1)
std_err = sem(pad2)
h = std_err * t.ppf((1 + confidence) / 2, n - 1)

start = m - h

end = m + h
print (start, end, start/m, end/m, m)
