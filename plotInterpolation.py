import sys
import os
import numpy as np


import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import dweibull
from matplotlib import rc

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
nbVox = int(filenames[len(filenames) - 1])
# 0 is the script name
for i in range(1, len(filenames) - 1):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    values.append(value/nbVox)
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
        ax.plot(values[i], zcs[i], label= "voxel 10cm", linewidth=0.7) 
    elif i == 1 :
        #ax.plot(values[i], zcs[i], '.-', label= "voxel 10cm + 40cm") 
        ax.plot(values[i], zcs[i], label= "voxel 10cm + 40cm", linewidth=0.7, color='black') 
    else :
        ax.plot(values[i], zcs[i], label= "Reference L-Architect", linewidth=0.7) 
 
#par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)

ax.legend()

xlabel = "PAD ($m^2.m^{-3}$)"
ylabel = "Height (m)"
base = os.path.splitext(filenames[1])[0]
outfile = base.split(os.path.sep)[0] + "-10cm40cmf.pdf"
fig.savefig(outfile)

