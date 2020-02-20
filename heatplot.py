import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import colors
A = np.loadtxt('data.txt')
mask = np.zeros_like(A)
mask[np.tril_indices_from(mask)] = True
mask[np.diag_indices_from(mask)] = False
xlabels = ['1', '2', '3','4','5','6','7','8']
cbar_kws={"ticks":[70.0,46.0,22.0,-2.0,-26.0,-50.0,-72.0],"orientation":"horizontal","shrink":.7}
annot_kws={"size":8}
cmap=plt.cm.RdYlBu
im = sns.heatmap(A,mask=mask,cmap=cmap,annot=True,xticklabels=xlabels,yticklabels=xlabels,fmt=".2f",cbar=True,vmax=70.0,vmin=-72.0,square=True,linewidths=.2,linecolor="grey",cbar_kws=cbar_kws,annot_kws=annot_kws,linestyle="-")
im.tick_params(left=False, right=True, top=True, bottom=False, labelleft=False, labelright=True, labeltop=True, labelbottom=False,direction="out",labelsize=10)
im.set_yticklabels(xlabels,va="center")
plt.style.use('classic')
plt.tight_layout()
sns.set_context('paper')
im.get_figure().savefig("data.png",dpi=300)



