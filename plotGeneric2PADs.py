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

MAX_PAD = 0.4
MAX_Z = 25
zcs = []
values = []
#maxPad = []
minZ = sys.float_info.max
maxZ = -sys.float_info.max;
label1 = filenames[len(filenames) - 2]
label2 = filenames[len(filenames) - 1]
# 0 is the script name
for i in range(1, len(filenames) -2):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    values.append(value)
    #maxPad.append(max(value))
    tmpMinZ = min(zc) 
    tmpMaxZ = max(zc)
    if tmpMinZ < minZ:
        minZ = tmpMinZ

    if tmpMaxZ > maxZ:
        maxZ = tmpMaxZ

#maxOfMax = max(maxPad)

ax = plt.axes()

ax.set_ylim(minZ + 2.5, MAX_Z)
ax.set_xlim(0, MAX_PAD)

ax.set_xlabel("PAD ($m^2.m^{-3}$)")
ax.set_ylabel("Height (m)")

for i in range(0, len(values)) :

    if i == 0 :
        ax.plot(values[i], zcs[i], label= label1,linewidth=0.8, color=palettes["PAD"])
    elif i == 1 :
        ax.plot(values[i], zcs[i], linestyle='--', label= label2,linewidth=0.8, color=palettes["PAD"])

#par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)

ax.legend()

outfile = "/tmp/generic.pdf"
fig.savefig(outfile)

outfile = "/tmp/generic.png"
fig.savefig(outfile)

