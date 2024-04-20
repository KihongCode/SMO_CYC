import numpy as np
import matplotlib.pyplot as plt
import tol_colors as tc
from pdb3 import lsext
import mplhelv
from tqdm.notebook import tqdm
tol_cmap = tc.tol_cmap('rainbow_PuBr')
import pickle
from free_energy_plot import free_energy_plot, gap

## Load MSM weights

weights = np.concatenate(pickle.load(open(f'../../MSM_Construction/19/Dtraj_Weights/weights_150_40.pkl','rb')))

## Load npy files

npys = lsext('./DREnpy/','.npy')[0] +lsext('../PROJ14952/DREnpy/','.npy')[0]
total_data = []
for npy in tqdm(npys):
    y = np.load(npy)
    total_data.append(y)


total_data_con = np.concatenate(total_data)

## Construct Free Energy Plot for D-R distance vs. W-M distance (corresponds to 1st and 0th distance)

l = free_energy_plot(total_data_con[:,1]*10,total_data_con[:,0]*10, vmax = 7, weightsClassA = weights)
l[1].set_xlabel('R400 -- D473 (Å)',fontsize=20)
l[1].set_ylabel('W339 -- M449 (Å)',fontsize=20)
l[1].set_ylim(1,13)
yticks = range(1,14,2)
l[1].set_yticks(yticks)

l[1].set_xlim(1,11)
xticks = range(1,12,2)
l[1].set_xticks(xticks)
l[1].set_title('Cyclopamine bound to TMD', fontsize = 20)
l[1].scatter(data1[0][1]*10,  data1[0][0]*10, marker='*', s=100, facecolors='k', edgecolors='r')
l[1].scatter(data3[0][1]*10,  data3[0][0]*10, marker='d', s=100, facecolors='k', edgecolors='r')
