import sys
import os
import numpy as np


import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import dweibull
from matplotlib import rc

from utils import palettes

plt.style.use('seaborn-whitegrid')

matplotlib.rcParams.update({'font.size': 11})
#matplotlib.rcParams.update({'text.latex.unicode': True}) #rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})

matplotlib.rcParams['font.family'] = 'sans-serif'

fig = plt.figure(1)
filenames = sys.argv

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)

#file 1 PAD
#file 2 Ref
#file 3 RDI
#file 4 Points

zcs = []
values = []
maxPad = []
minZ = sys.float_info.max
maxZ = -sys.float_info.max;
print (filenames)
nbvox = []
nbvox.append(0) #dummy
nbvox.append(int(filenames[5]))
nbvox.append(int(filenames[6]))
nbvox.append(int(filenames[7]))
nbvox.append(int(filenames[8]))

# 0 is the script name
for i in range(1, 5):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    values.append(value/nbvox[i])
    maxPad.append(max(value))
    tmpMinZ = min(zc) 
    tmpMaxZ = max(zc)
    if tmpMinZ < minZ:
        minZ = tmpMinZ

    if tmpMaxZ > maxZ:
        maxZ = tmpMaxZ

maxOfMax = max(maxPad)

ax = plt.axes()

ax.set_xlabel("PAD ($m^2.m^{-3}$)")
ax.set_ylabel("Height (m)")

for i in range(0, len(values)) :
    if i == 0:
        ax.plot(values[i], zcs[i], label= "voxel 10 cm", linewidth=0.8, color=palettes["PAD"]) 
    elif i == 1 :
        #ax.plot(values[i], zcs[i], '.-', label= "voxel 10cm + 40cm") 
        ax.plot(values[i], zcs[i], label= "voxel 20 cm", linestyle='--', linewidth=0.8, color=palettes["PAD"]) 
    elif i == 2 :
        #ax.plot(values[i], zcs[i], '.-', label= "voxel 10cm + 40cm") 
        ax.plot(values[i], zcs[i], label= "voxel 40 cm", linestyle='--', marker='+', linewidth=0.8, color=palettes["PAD"]) 
    else :
        ax.plot(values[i], zcs[i], label= "L-Architect", linewidth=0.8, color = palettes["L-Architect"]) 
 

#par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)

MAX_X = 0.4
ax.set_ylim(0, 16)
ax.set_xlim(0, MAX_X)
ax.legend()

fig.set_size_inches(6, 6)
xlabel = "PAD ($m^2.m^{-3}$)"
ylabel = "Height (m)"
outfile = "/tmp/voxelsizes.pdf"
fig.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)

#plt.show()
