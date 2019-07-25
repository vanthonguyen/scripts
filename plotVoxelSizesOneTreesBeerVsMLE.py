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
NB_VOX = 15 * 14

fig = plt.figure()
ax = plt.axes()
filenames = sys.argv

zcs = []
values = []
minZ = sys.float_info.max
maxZ = -sys.float_info.max;
# 0 is the script name
for i in range(1, len(filenames)):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    values.append(value/NB_VOX)


labels = np.array(5)
smallestVox = 2.5

#maxOfMax = max(maxPad)
for i in range(0, len(values)) :
    voxSize = smallestVox * 2**i
    #ratio = maxOfMax / maxPad[i]
    #for j in range(0, len(values[i])) :
    #    values[i][j] = values[i][j] * ratio
    voxStr = str(voxSize)
    if voxSize.is_integer() :
        voxStr = str(int(voxSize))
    labelStr = "voxel " + voxStr + " cm"
    ax.plot(values[i], zcs[i], label= labelStr, linewidth=0.7) 
    #if i == 0 :
    #    ax.plot(values[i], zcs[i], label= "voxel 2.5 cm", linewidth=0.8, color=palettes["PAD"]) 
    #if i == 1 :
    #    ax.plot(values[i], zcs[i], label= "voxel 5 cm", linestyle='--', linewidth=0.8, color=palettes["PAD"]) 
    #if i == 2 :
    #    #ax.plot(values[i], zcs[i], label= "voxel 40 cm", linestyle=':', marker='.', linewidth=0.8, color=palettes["PAD"]) 
    #    ax.plot(values[i], zcs[i], label= "voxel  cm", linestyle=':', marker='+', linewidth=0.8, color=palettes["PAD"]) 
        #ax.plot(values[i], zcs[i], label= "40 cm")
    #weibull

#filename2 = sys.argv[2]
#filename3 = sys.argv[2]

title = ""
xlabel = "PAD"
ylabel = "z (m)"
ax.legend()
#ax.set_xlim(0, MAX_PAD) 
#ax.set_ylim(0, MAX_Z)

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
outfile = "/tmp/onetreeVoxSizes.pdf"
fig.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)
#plt.show()
