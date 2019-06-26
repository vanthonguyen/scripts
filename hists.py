#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sys

#fig = plt.figure()
#ax = plt.axes()
filenames = sys.argv


intensities = []
labels=[]

bins = np.linspace(-1, 1, 200)
# 0 is the script name
for i in range(1, len(filenames)):
    #read value
    ints = np.loadtxt(filenames[i], dtype='float', delimiter=' ', usecols=(2), unpack=True, skiprows=0)
    intensities.append(ints.tolist())
    labels.append(filenames[i])

#print(labels)
#print(intensities)
plt.hist(intensities, 20, density=False, histtype='bar', label=labels)
#$plt.hist(intensities, bins, labels)
plt.legend(prop={'size': 10})

plt.xlabel('Intensity')
plt.ylabel('Frequency')
#plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()
