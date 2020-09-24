import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import colors
A = np.loadtxt('fftAll.dat')
x,y1,y2,y3=A.T
plt.scatter(x, -(y1+y2+y3))
plt.xlim(0,6)
plt.savefig("fullspectra.png",dpi=300)
