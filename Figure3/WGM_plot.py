import numpy as np
import tol_colors as tc
from pdb3 import lsext
import mplhelv
from tqdm.notebook import tqdm
from free_energy_plot import free_energy_plot, gap
tol_cmap = tc.tol_cmap('rainbow_PuBr')
import pickle


## Load the .npy files

npys = lsext('../../MSM_Construction/19/57npy_14940/','.npy')[0]+lsext('../../MSM_Construction/19/57npy_14952/','.npy')[0]
total_data = []
for npy in tqdm(npys):
    y = np.load(npy)
    total_data.append(y)
total_data_con = np.concatenate(total_data)



## Load the weights

weights = np.concatenate(pickle.load(open(f'../../MSM_Construction/19/Dtraj_Weights/clus_tica_dtrajs_150_40.pkl','rb')))

## Construct Free Energy plot for WGM motif (corresponds to 33rd and 34th distance)

l = free_energy_plot(total_data_con[:,33]*10,total_data_con[:,34]*10,vmax=6, weightsClassA=weights)
l[1].set_xlabel('W339 -- G422 (Å)',fontsize=20)
l[1].set_ylabel('W339 -- M449 (Å)',fontsize=20)
l[1].set_ylim(1,15)
yticks = range(1,16,2)
l[1].set_yticks(yticks)
l[1].set_xlim(1,13)
xticks = range(1,14,2)
l[1].set_xticks(xticks)
l[1].scatter(data1[0][4]*10,  data1[0][0]*10, marker='*', s=100, facecolors='k', edgecolors='r', label = 'Inactive')
l[1].scatter(data3[0][4]*10,  data3[0][0]*10, marker='d', s=100, facecolors='k', edgecolors='r', label = 'Active')
l[1].legend(fontsize=20,frameon=False)
l[0].savefig('/home/pdb3/kihongk2/Images/System19_WGM.png',transparent=True,dpi=300)
