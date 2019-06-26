import re
import sys
import math

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from scipy import mean

filename1 = sys.argv[1]
filename2 = sys.argv[2]

skip = 22
if len(sys.argv) > 3 :
    skip += int(sys.argv[3])

#ref
#pad1 = np.loadtxt(filename1, dtype='float', delimiter='\t', usecols=(0), unpack=True, skiprows=skip)
pad1 = pd.read_csv(filename1, skiprows=skip, header=None)[0]

#print (pad1)
#quit()
#est
#pad2 = np.loadtxt(filename2, dtype='float', delimiter='\t', usecols=(0), unpack=True, skiprows=skip)
pad2 = pd.read_csv(filename2, skiprows=skip, header=None)[0]
if len(pad1) > len(pad2):
    pad1 = pad1[:len(pad2)]
elif len(pad2) > len(pad1):
    pad2 = pad2[:len(pad1)]

r2 = r2_score(pad1, pad2)

rmse = math.sqrt(mean_squared_error(pad1, pad2))
mea = mean_absolute_error(pad1, pad2)
#m = pad1.mean(dtype=np.float64)
m = mean(pad1)
bias = mean(pad2 - pad1)

#n = len(pad1)
#m = pad1.sum()/n
rrmse = rmse/m


print ("r2=%f, rmse=%f, rrmse=%f, mean=%f, mea=%f, bias=%f" % (r2,rmse, rrmse,m,mea,bias))
