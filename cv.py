import re
import sys
import math

import numpy as np
from sklearn.metrics import r2_score

filename1 = sys.argv[1]
filename2 = sys.argv[2]

pad1 = np.loadtxt(filename1, dtype='float', delimiter='\t', usecols=(5), unpack=True, skiprows=11)
pad2 = np.loadtxt(filename2, dtype='float', delimiter='\t', usecols=(5), unpack=True, skiprows=11)

r2 = r2_score(pad1, pad2)
print r2
