import sys
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import dweibull
from matplotlib import rc

plt.style.use('seaborn-whitegrid')


matplotlib.rcParams.update({'font.size': 14})
#matplotlib.rcParams.update({'text.latex.unicode': True}) #rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})

matplotlib.rcParams['font.family'] = 'sans-serif'

fig = plt.figure()
ax = plt.axes()
filenames = sys.argv

MAX_PAD = 0.4
MAX_Z = 25
zcs = []
values = []
minZ = sys.float_info.max
maxZ = -sys.float_info.max;
# 0 is the script name
for i in range(1, 3):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    values.append(value)
    #maxPad.append(max(value))
    tmpMinZ = sys.float_info.max
    tmpMaxZ = sys.float_info.min
 
    for ind in range(0, len(value)) :
        val = value[ind]
        zval = zc[ind]
        if val > 0 and zval < tmpMinZ :
            tmpMinZ = zval
        if zval > tmpMaxZ :
            tmpMaxZ = zval

    if tmpMinZ < minZ:
        minZ = tmpMinZ

    if tmpMaxZ > maxZ:
        maxZ = tmpMaxZ
print (minZ, maxZ)

# normalize to sol = 0m
# minZ <=> 0

for i in range (0, len(zcs)):
    zcs[i] -= minZ

maxZ = maxZ - minZ + 1
minZ = -1

nbScans = sys.argv[3]
#maxOfMax = max(maxPad)
for i in range(0, len(values)) :
    #ratio = maxOfMax / maxPad[i]
    #for j in range(0, len(values[i])) :
    #    values[i][j] = values[i][j] * ratio
    if i == 0 :
        ax.plot(values[i], zcs[i], label= nbScans + " scans")
    if i == 1 :
        ax.plot(values[i], zcs[i], label= "center scan")
    #weibull

#filename2 = sys.argv[2]
#filename3 = sys.argv[2]

title = ""
xlabel = "PAD"
ylabel = "z (m)"
ax.legend()
ax.set_xlim(0, MAX_PAD) 
ax.set_ylim(1.5, MAX_Z)
#minor_ticks = np.arange(int(minZ), maxZ)
#ax.set_yticks(minor_ticks, minor=True)
ax.grid(which='both')
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)


#print "its me"


plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel);

fig.set_size_inches(6, 6)
#base = os.path.splitext(filenames[1])[0]
outfile = "allvs0.pdf"
fig.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)
#plt.show()
