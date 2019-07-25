import sys
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import dweibull
from matplotlib import rc
from utils import palettes

plt.style.use('seaborn-whitegrid')


matplotlib.rcParams.update({'font.size': 14})
#matplotlib.rcParams.update({'text.latex.unicode': True}) #rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})

matplotlib.rcParams['font.family'] = 'sans-serif'



MAX_PAD = 0.4
MAX_Z = 25

fig = plt.figure()
ax = plt.axes()
filenames = sys.argv
nbvox = int(filenames[5])

zcs = []
values = []
minZ = sys.float_info.max
maxZ = -sys.float_info.max;
# 0 is the script name
for i in range(1, len(filenames) -1 ):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    values.append(value/nbvox)
    #maxPad.append(max(value))
    tmpMinZ = sys.float_info.max
    tmpMaxZ = sys.float_info.min
 
    for ind in range(0, len(value)) :
        val = value[ind]
        zval = zc[ind]
        if val > 0 and zval > tmpMaxZ :
            tmpMaxZ = zval
        if zval < tmpMinZ :
            tmpMinZ = zval


    if tmpMinZ < minZ:
        minZ = tmpMinZ

    if tmpMaxZ > maxZ:
        maxZ = tmpMaxZ

# normalize to sol = 0m
# minZ <=> 0

for i in range (0, len(zcs)):
    zcs[i] -= minZ

print (zcs)
maxZ = maxZ - minZ + 1
minZ = -1
print (minZ, maxZ)

#maxOfMax = max(maxPad)
for i in range(0, len(values)) :
    #ratio = maxOfMax / maxPad[i]
    #for j in range(0, len(values[i])) :
    #    values[i][j] = values[i][j] * ratio
    if i == 0 :
        ax.plot(values[i], zcs[i], label= "One scan", linestyle='--', linewidth=0.8, color=palettes["PAD"]) 
    if i == 1 :
        ax.plot(values[i], zcs[i], label= "One scan + interpolation", linewidth=0.8, color=palettes["Point"]) 
    if i == 2 :
        ax.plot(values[i], zcs[i], label= "All 5 scans",linewidth=0.8, color=palettes["PAD"]) 
    if i == 3 :
        ax.plot(values[i], zcs[i], label= "L-Architect PAD",linewidth=0.8, color=palettes["L-Architect"])
        #ax.plot(values[i], zcs[i], label= "40 cm")
    #weibull

#filename2 = sys.argv[2]
#filename3 = sys.argv[2]

title = ""
xlabel = "PAD"
ylabel = "z (m)"
ax.legend()
ax.set_xlim(0, MAX_PAD) 
ax.set_ylim(0, MAX_Z)

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
outfile = "/tmp/inter.pdf"
fig.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)
#plt.show()
