import sys
import os
import numpy as np


from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes                                                                                                                                                                        

import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import dweibull
from matplotlib import rc

plt.style.use('seaborn-whitegrid')

matplotlib.rcParams.update({'font.size': 14})
#matplotlib.rcParams.update({'text.latex.unicode': True}) #rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})

matplotlib.rcParams['font.family'] = 'sans-serif'

fig = plt.figure()
filenames = sys.argv

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)


zcs = []
values = []
maxPad = []
minZ = sys.float_info.max
maxZ = -sys.float_info.max;
# 0 is the script name
for i in range(1, len(filenames)):
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

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par2 = ParasiteAxes(host, sharey=host)   
host.parasites.append(par2)

host.set_xlabel("PAD ($m^2.m^{-3}$)")
host.set_ylabel("Height (m)")

par2.set_xlabel("Points")
new_axisline = par2._grid_helper.new_fixed_axis
par2.axis["top"] = new_axisline(loc="top", axes=par2)
fig.add_axes(host)

for i in range(0, len(values)) :
    ratio = maxOfMax / maxPad[i]
    #for j in range(0, len(values[i])) :
    #    values[i][j] = values[i][j] * ratio
    if i < len(values) - 1 :
        host.plot(values[i], zcs[i], label= os.path.splitext(os.path.basename(filenames[i + 1]))[0])
    else :
        par2.plot(values[i], zcs[i], label= os.path.splitext(os.path.basename(filenames[i + 1]))[0])
 
#par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)

host.legend()

#host.axis["bottom"].label.set_color(p1.get_color())
#par1.axis["top"].label.set_color(p1.get_color())
#par2.axis["top"].label.set_color(p2.get_color())

title = filenames[1]

plt.show()

