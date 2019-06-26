import re
import sys
import math

import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

filename1 = sys.argv[1]
filename2 = sys.argv[2]
skip = 11
if len(sys.argv) > 3 :
    skip += int(sys.argv[3])

pad1 = np.loadtxt(filename1, dtype='float', delimiter='\t', usecols=(5), unpack=True, skiprows=skip)
pad2 = np.loadtxt(filename2, dtype='float', delimiter='\t', usecols=(5), unpack=True, skiprows=skip)
if len(pad1) > len(pad2):
    pad1 = pad1[:len(pad2)]
elif len(pad2) > len(pad1):
    pad2 = pad2[:len(pad1)]

r2 = r2_score(pad1, pad2)

rms = math.sqrt(mean_squared_error(pad1, pad2))
mae = mean_absolute_error(pad1, pad2)
m = np.mean(pad1)
bias = np.mean(pad2 - pad1)
rrmse = rms/m
print ("r2=%f, rmse=%f, rrmse=%f, mean=%f, mae=%f, bias=%f" % (r2,rms,rrmse,m,mae,bias))
