import sys
import numpy as np
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
import matplotlib.pyplot as plt
import matplotlib.cm as cm

filename1 = sys.argv[1]

pad1,pad2,ocl = np.loadtxt(filename1, dtype='float', delimiter='\t', usecols=(0,1,2), unpack=True, skiprows=0)

# seed random number generator
seed(1)
# prepare data
data1 = pad2 - pad1
data2 = 1 - ocl
# summarize
# plot
#idx=random.sample(range(len(data1),1000))

xlabel = "pad - pad L-Architect"
ylabel = "(nt - nb)/nt"

plt.xlabel(xlabel)
plt.ylabel(ylabel);

plt.scatter(data2,data1,alpha=0.5, color='black')
#plt.show()

outfile = "error.pdf"
plt.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)
