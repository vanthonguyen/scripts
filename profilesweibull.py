import sys
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
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
for i in range(0, len(values)) :
    ratio = maxOfMax / maxPad[i]
    #for j in range(0, len(values[i])) :
    #    values[i][j] = values[i][j] * ratio
    ax.plot(values[i], zcs[i], label= os.path.splitext(os.path.basename(filenames[i + 1]))[0])

#filename2 = sys.argv[2]
#filename3 = sys.argv[2]

title = filenames[1]
xlabel = "PAD"
ylabel = "z (m)"
ax.legend()
ax.set_ylim(minZ, maxZ)
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel);

fig.set_size_inches(6, 9)
base = os.path.splitext(filenames[1])[0]
outfile = base + "multi-normalized.pdf"
fig.savefig(outfile)
#plt.show()
