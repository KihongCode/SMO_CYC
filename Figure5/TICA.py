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
from free_energy_plot import free_energy_plot, gap

tol_cmap = tc.tol_cmap('rainbow_PuBr')


## load the 57 computed distances of inactive & active pdb structures

data1 = np.load('Sys8_HMass_Distances.npy')[0]
data2 = np.load('Sys2_HMass_Distances.npy')[0]
projection1 = tica.transform(data1)
projection2 = tica.transform(data2)

## load the MSM weights

weights = np.concatenate(pickle.load(open(f'./Dtraj_Weights/weights_150_40.pkl','rb')))


## load the 57 computed distances of inactive & active MD trajectories

npys = lsext('./57npy_14953/','.npy')[0]+lsext('./57npy_14941/','.npy')[0]

total_data = []
for npy in tqdm(npys):
    y = np.load(npy)
    total_data.append(y)

## construct tica using TICA function

tica = TICA(lagtime=300, var_cutoff=40/100).fit_fetch(np.concatenate(total_data))

projection = [tica.transform(x) for x in total_data]

tica_concatenated = np.concatenate(projection)

# use free_energy_plot function to plot the first 2 tICA components

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
