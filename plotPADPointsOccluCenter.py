import sys
import os
import numpy as np


from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes                                                                                                                                                                        

import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import dweibull
from matplotlib import rc

from utils import palettes

plt.style.use('seaborn-whitegrid')

matplotlib.rcParams.update({'font.size': 10})
#matplotlib.rcParams.update({'text.latex.unicode': True}) #rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})

MAX_PAD = 0.4
MAX_Z = 25
matplotlib.rcParams['font.family'] = 'sans-serif'

fig = plt.figure(1)
filenames = sys.argv

skipZ = float(filenames[len(filenames) - 2])
maxPoints = int(filenames[len(filenames) - 1])

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)

#file 1 PAD
#file 2 Ref
#file 3 RDI
#file 4 Points
res=0.1
zcs = []
values = []
maxVal = np.zeros(len(filenames))
minEffZ = skipZ
nbSkip = minEffZ/res

minZ = sys.float_info.max
maxZ = -sys.float_info.max

# 0 is the script name
for i in range(1, len(filenames) - 2):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    tmpMinZ = sys.float_info.max
    tmpMaxZ = sys.float_info.min
    for ind in range(0, len(value)) :
        val = value[ind]
        zval = zc[ind]
        #skip ground value
        if ind > nbSkip and val > maxVal[i]:
            maxVal[i] = val
        if zval < tmpMinZ :
            tmpMinZ = zval
 
        #dont' count maxZ of occlu
        if val > 0 and i < len(filenames) - 2:
           if zval > tmpMaxZ :
                tmpMaxZ = zval
    values.append(value)
    if tmpMinZ < minZ:
        minZ = tmpMinZ

    if tmpMaxZ > maxZ:
        maxZ = tmpMaxZ



for i in range (0, len(zcs)):
    zcs[i] -= minZ

maxZ = maxZ - minZ + 2
#minZ = minEffZ

#print (zcs)
#print (values)

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharey=host)   
par2 = ParasiteAxes(host, sharey=host)   
host.parasites.append(par1)
host.parasites.append(par2)

host.set_xlabel("PAD ($m^2.m^{-3}$)")
host.set_ylabel("Height (m)")
host.set_xlim(0, MAX_PAD)

par1.set_xlabel("Average number of returns per 10cm cube voxel")
#par1.set_xlabel("RDI")
par2.set_xlabel("Occusion (%)")

host.axis["top"].set_visible(False)
par1.axis["top"].set_visible(True)
par1.axis["top"].major_ticklabels.set_visible(True)
par1.axis["top"].label.set_visible(True)
#par2.axis["top"].label.set_visible(True)
par1.set_xlim(0,maxVal[2]/maxVal[1]*MAX_PAD)

offset = (0, 40)
new_axisline = par2._grid_helper.new_fixed_axis
par2.axis["top2"] = new_axisline(loc="top", axes=par2, offset=offset)
par2.axis["top2"].set_visible(True)
par2.axis["top2"].major_ticklabels.set_visible(True)

par2.set_xlim(0,100)

fig.add_axes(host)

for i in range(0, len(values)) :
    #for j in range(0, len(values[i])) :
    #    values[i][j] = values[i][j] * ratio
    if i == 0 :
        h, = host.plot(values[i], zcs[i], label= "PAD - all scans",linewidth=0.8, color=palettes["PAD"])
    elif i == 1 :
        host.plot(values[i], zcs[i], linestyle='--', label= "PAD - center scan",linewidth=0.8, color=palettes["PAD"])
    elif i == 2 :
        p1, = par1.plot(values[i], zcs[i], label= "number of returns", linewidth=0.8, color=palettes["Point"])
        #p1, = par1.plot(values[i], zcs[i], label= "Nb of returns", linewidth=0.8, color=palettes["Point"])
    else :
        p2, = par2.plot(values[i]*100, zcs[i], label= "Occlusion)", linewidth=0.8, color=palettes["Occlusion"])
 
#par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)

host.legend()


par1.axis["top"].major_ticklabels.set_color(p1.get_color())
par2.axis["top2"].major_ticklabels.set_color(p2.get_color())
host.axis["bottom"].major_ticklabels.set_color(h.get_color())

par1.axis["top"].label.set_color(p1.get_color())
par2.axis["top2"].label.set_color(p2.get_color())
host.axis["bottom"].label.set_color(h.get_color())

#host.axis["bottom"].label.set_color(p1.get_color())
host.set_ylim(1.5, MAX_Z)
par1.set_xlim(0,maxPoints)


#fig.set_size_inches(6, 6)
#plt.show()
outfile = "/tmp/padvspointsvsocclu.pdf"
fig.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)

outfile = "/tmp/padvspointsvsocclu.png"
fig.savefig(outfile)

