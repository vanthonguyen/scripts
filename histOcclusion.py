#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from cycler import cycler
import sys

fig = plt.figure()
#ax = plt.axes()
filenames = sys.argv


intensities = []
labels=[]
colors=[]
weights=[]

#bar_cycle = (cycler('hatch', ['///', '--', '...','\///', 'xxx', '\\\\']) * cycler('color', 'w')*cycler('zorder', [10]))
#bar_cycle = (cycler('hatch', ['///', '\\\\\\', 'xxx']) * cycler('color', 'w')*cycler('zorder', [10]))
#styles = bar_cycle()

# 0 is the script name
for i in range(1, len(filenames)):
    #read value
    ints = np.loadtxt(filenames[i], dtype='float', delimiter=' ', usecols=(0), unpack=True, skiprows=0)
    intensities.append(ints.tolist())
    labels.append(filenames[i])
    ws = []
    w = len(ints) 
    for i in range(0, w) :
        ws.append(1.0/w)

    weights.append(ws)


#print("xxx")
#print(labels)
#print(intensities)
hists = plt.hist(intensities, 100, weights=weights, histtype='bar', label=labels)

#hists = plt.hist(intensities, 100, histtype='bar', label=labels)
print (hists)
#$plt.hist(intensities, bins, labels)
plt.legend(prop={'size': 10})

plt.xlabel('occlusion (%): (1-(nt-nb)/nt)*100')
plt.ylabel('Weighted proportion')
#plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
fig.savefig("occlusion.pdf")

#plt.show()
