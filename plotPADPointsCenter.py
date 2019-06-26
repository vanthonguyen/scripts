import sys
import os
import numpy as np


from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes                                                                                                                                                                        
from utils import palettes

import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import dweibull
from matplotlib import rc

plt.style.use('seaborn-whitegrid')

matplotlib.rcParams.update({'font.size': 14})
#matplotlib.rcParams.update({'text.latex.unicode': True}) #rc('font',**{'family':'sans-serif','sans-serif':['Source Sans Pro']})

matplotlib.rcParams['font.family'] = 'sans-serif'

fig = plt.figure(1)
filenames = sys.argv

MAX_X = 0.4

nbVox = int(filenames[len(filenames) - 2])
pointCoeff = float(filenames[len(filenames) - 1])
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
# 0 is the script name
for i in range(1, len(filenames) - 2):
    #read value
    zc, value = np.loadtxt(filenames[i], dtype='float, float', delimiter='\t', usecols=(4, 5), unpack=True, skiprows=11)
    zcs.append(zc)
    #if i == 3 :
    #    values.append(value/nbVox/pointCoeff)
    #else :
    values.append(value/nbVox)
    maxPad.append(max(value))
    tmpMinZ = min(zc) 
    tmpMaxZ = max(zc)
    if tmpMinZ < minZ:
        minZ = tmpMinZ

    if tmpMaxZ > maxZ:
        maxZ = tmpMaxZ

maxOfMax = max(maxPad)

host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
par1 = ParasiteAxes(host, sharey=host)   
par2 = ParasiteAxes(host, sharey=host)   
host.parasites.append(par1)
host.parasites.append(par2)

host.set_xlabel("PAD ($m^2.m^{-3}$)")
host.set_ylabel("Height (m)")

#par1.set_xlabel("RDI")
par1.set_xlabel("Average number of returns per 10cm cube voxel")

host.axis["top"].set_visible(False)
par1.axis["top"].set_visible(True)
par1.axis["top"].major_ticklabels.set_visible(True)
par1.axis["top"].label.set_visible(True)

#offset = (0, 40)
#new_axisline = par2._grid_helper.new_fixed_axis
#par2.axis["top2"] = new_axisline(loc="top", axes=par2, offset=offset)

fig.add_axes(host)

for i in range(0, len(values)) :
    ratio = maxOfMax / maxPad[i]
    #for j in range(0, len(values[i])) :
    #    values[i][j] = values[i][j] * ratio
    if i == 0 :
        host.plot(values[i], zcs[i], label= "PAD - all scans",linewidth=0.8, color=palettes["PAD"])
    elif i == 1 :
        host.plot(values[i], zcs[i], linestyle='--', label= "PAD - center scan",linewidth=0.8, color=palettes["PAD"])
    elif i == 2 : p1, = par1.plot(values[i], zcs[i], label= "number of returns", linewidth=0.8, color=palettes["Point"])

        #host.plot(values[i], zcs[i], label= "number of returns")

    #elif i == 2 :
    #elif i < len(values) - 1 :
        #p1, = par1.plot(values[i], zcs[i], label= os.path.splitext(os.path.basename(filenames[i + 1]))[0])
    #    p1, = par1.plot(values[i], zcs[i], label= "RDI")
    elif i == 3:
        host.plot(values[i], zcs[i], label= "L-Architect PAD",linewidth=0.8, color = palettes["L-Architect"])
 
#par1.set_ylim(0, 16)
#par2.set_ylim(1, 65)

host.set_ylim(0, 16)
host.set_xlim(0, MAX_X)
host.legend()

#p1
#maxPoints = 
if max(values[2]) < 3:
    par1.set_xlim(0,8)

#remove decima if it is integer
#pointsXlabels = par1.get_xticks().tolist()
#pointsTicklabels = []
#for lab in pointsXlabels: 
#    newtick = float(lab)
#    newtickstring = str(float(newtick))
#    if newtick.is_integer() :
#        newtickstring = str(int(newtick))
#        
#    pointsTicklabels.append(newtickstring)
#par1.set_xlabel(newtickstring)

par1.axis["top"].label.set_color(p1.get_color())
#par2.axis["top2"].label.set_color(p2.get_color())
#host.axis["bottom"].label.set_color(p1.get_color())

#title = filenames[1]

fig.set_size_inches(6, 6)
#plt.show()
outfile = "/tmp/padvspoints.pdf"
fig.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)

outfile = "/tmp/padvspoints.png"
fig.savefig(outfile)
