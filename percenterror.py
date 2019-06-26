import re
import sys
import math

import numpy as np

filename1 = sys.argv[1]
filename2 = sys.argv[2]

pad1 = np.loadtxt(filename1, dtype='float', delimiter='\t', usecols=(0), unpack=True, skiprows=0)
pad2 = np.loadtxt(filename2, dtype='float', delimiter='\t', usecols=(0), unpack=True, skiprows=0)
print (pad2 - pad1)
