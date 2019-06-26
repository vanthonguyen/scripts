import sys
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import dweibull
from matplotlib import rc

plt.style.use('seaborn-whitegrid')


matplotlib.rcParams.update({'font.size': 14})
#matplotlib.rcParams.update({'text.latex.unicode': True})
#rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})

matplotlib.rcParams['font.family'] = 'sans-serif'

fig = plt.figure()
ax = plt.axes()
filenames = sys.argv

zcs = []
values = []
maxPad = []
minZ = sys.float_info.max
maxZ = -sys.float_info.max;
# 0 is the script name
for i in range(1, len(filenames) - 1):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    values.append(value)
    maxPad.append(max(value))
    tmpMinZ = min(zc) 
    tmpMaxZ = max(zc)
    if tmpMinZ < minZ:
        minZ = tmpMinZ

    if tmpMaxZ > maxZ:
        maxZ = tmpMaxZ

maxOfMax = max(maxPad)
ax.plot(values[0], zcs[0], label= "scan 0")
ax.plot(values[1], zcs[1], label= "scan all")
ax.plot(values[2], zcs[2], label= "scan 1234")
ax.plot(values[3], zcs[3], label= "Larchitect")


#filename2 = sys.argv[2]
#filename3 = sys.argv[2]

title = filenames[len(filenames) - 1]
xlabel = "PAD"
ylabel = "z (m)"
ax.legend()
ax.set_ylim(minZ, maxZ)
minor_ticks = np.arange(int(minZ), maxZ)
ax.set_yticks(minor_ticks, minor=True)
ax.grid(which='both')
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)


#print "its me"


plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel);

fig.set_size_inches(6, 9)
base = os.path.splitext(filenames[1])[0]
outfile = base + ".pdf"
fig.savefig(outfile)
#plt.show()
