import sys
import numpy as np
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
from sklearn.linear_model import LinearRegression

filename1 = sys.argv[1]

#pad1,pad2,ocl = np.loadtxt(filename1, dtype='float', delimiter='\t', usecols=(0,1,2), unpack=True, skiprows=0)
#pad1,pad2,ocl = np.genfromtxt(filename1, dtype='float', delimiter='\t', usecols=(0,1,2), unpack=True, skip_header=0)

df = pd.read_csv(filename1, delimiter="\t", skiprows=0, header=None).values
#
#print(df.head())
#df.plot(figsize=(18,5))



# seed random number generator
seed(1)
# prepare data
y = df[:,1] - df[:,0]
#x = (1 - ocl).reshape((-1, 1))
x = (1 - df[:,2]).reshape((-1, 1))

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

samples = df[np.random.choice(df.shape[0], 100000, replace=False), :]
intercept = float(model.intercept_)
slope = float(model.coef_)
line = slope*samples[:,2]+intercept

#random
#print (samples[:,2])
# Plot outputs

matplotlib.rcParams.update({'font.size': 20})

plt.scatter(1 - samples[:,2], samples[:,1] - samples[:,0], color='black', alpha=0.5, s=10)
plt.plot(1 - samples[:,2], line, 'r', label="y={:.2f}x{:.2f}, $R^2$={:.4f}".format(slope,intercept,r_sq), linewidth=1,alpha=0.9)

ylabel = "estimated PAD - L-Architect"
xlabel = "(Nt - Nb)/Nt"

plt.xlabel(xlabel)
plt.ylabel(ylabel);


#plt.xticks(())
#plt.yticks(())
outfile = "errorPad.pdf"
plt.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)
plt.show()

# summarize
# plot
#idx=random.sample(range(len(data1),1000))

#xlabel = "pad - pad L-Architect"
#ylabel = "(nt - nb)/nt"
#
#plt.xlabel(xlabel)
#plt.ylabel(ylabel);
#
#plt.scatter(data2,data1,alpha=0.5, color='black')
##plt.show()
#
#outfile = "error.pdf"
#plt.savefig(outfile, bbox_inches = 'tight', pad_inches = 0)
