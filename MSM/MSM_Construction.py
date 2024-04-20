from pdb3 import lsext
from tqdm import tqdm
import deeptime
import numpy as np
import matplotlib.pyplot as plt
import tol_colors as tc
from pdb3 import lsext
import mplhelv
from tqdm import tqdm
from deeptime.decomposition import TICA
from deeptime.clustering import KMeans
import pickle


# load the computed distances of inactive & active ensembles using built-in 'lsext' function
npys = lsext('./inactive_distances/','.npy')[0]+lsext('./active_distances/','.npy')[0]

# store npys into total_data
total_data = []
for npy in tqdm(npys):
    y = np.load(npy)
    total_data.append(y)

# construct tica using TICA function
tica = TICA(lagtime=, var_cutoff=).fit_fetch(np.concatenate(total_data))

projection = [tica.transform(x) for x in total_data]

tica_concatenated = np.concatenate(projection)

# use free_energy_plot function to plot the first 2 tICA components (see SMO_CYC/MSM/free_energy_plot.py)
l = free_energy_plot(tica_concatenated[:,0],tica_concatenated[:,1],weightsClassA = weights, vmax = 7)
l[1].set_xlabel('time-lagged independent component 1',fontsize=20)
l[1].set_ylabel('time-lagged independent component 2',fontsize=20)



l[1].set_ylim(-3,11)
yticks = range(-3,12,2)
l[1].set_yticks(yticks)
l[1].set_xlim(-4,4)
xticks = range(-4,5,2)
l[1].set_xticks(xticks)




l[1].scatter(projection1[0],  projection1[1], marker='*', s=100, facecolors='k', edgecolors='r', label = 'Inactive')
l[1].scatter(projection2[0],  projection2[1], marker='d', s=100, facecolors='k', edgecolors='r', label = 'Active')
l[1].legend(fontsize=20,frameon=False,loc='upper left')
l[0].savefig("/home/pdb3/kihongk2/Images/TICA_82.png", dpi=300, transparent = True)
