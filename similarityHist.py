import sys
import numpy as np
from scipy.spatial import distance

filename1 = sys.argv[1]
filename2 = sys.argv[2]
pad1 = np.loadtxt(filename1, dtype='float', delimiter='\t', usecols=(5), unpack=True, skiprows=11)
pad2 = np.loadtxt(filename2, dtype='float', delimiter='\t', usecols=(5), unpack=True, skiprows=11)
dE = distance.euclidean(pad1, pad2)

rog = distance.rogerstanimoto(pad1,pad2)
print("Euclidean",dE)

print("Rogers",rog)
