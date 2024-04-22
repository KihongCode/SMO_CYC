import numpy as np
import pickle
import torch
import torch.nn as nn
from deeptime.util.torch import MLP
from deeptime.decomposition.deep import VAMPNet
from deeptime.util.data import TimeLaggedDataset
from deeptime.util.data import TimeLaggedConcatDataset
from deeptime.util.data import TrajectoryDataset
from torch.utils.data import DataLoader
import sys
from tqdm import tqdm
import sys
print(sys.path)
from natsort import natsorted
from pdb3 import lsext
if torch.cuda.is_available():
    device = torch.device("cuda")
    torch.backends.cudnn.benchmark = True
else:
    device = torch.device("cpu")
torch.set_num_threads(12)

num_meta = 6 

tau = 250

train_ratio = 0.7

npys = list(natsorted(lsext('./57npy_14942/','.npy')[0] + lsext('./57npy_14943/','.npy')[0]))

totdist = []
filename = []
for npy in npys:
    totdist.append(np.load(npy))
    filename.append(npy)
pickle.dump(filename, open(f'./traj_filenames_Dual_CYC_{num_meta}.pkl','wb'))
totdist_new = []
for dist in totdist:
    totdist_new.append(dist.astype('float32'))

dataset = TrajectoryDataset.from_trajectories(lagtime=300, data=totdist_new)
print(dataset.subsets[0].data)
n_val = int(len(dataset)*.3)
train_data, val_data = torch.utils.data.random_split(dataset, [len(dataset) - n_val, n_val])

print(len(dataset),type(train_data),type(val_data))

lobe = nn.Sequential(
    nn.BatchNorm1d(dist.shape[1]),
    nn.Linear(dist.shape[1], 30), nn.ELU(),
    nn.Linear(30, 100), nn.ELU(),
    nn.Linear(100, 100), nn.ELU(),
    nn.Linear(100, 100), nn.ELU(),
    nn.Linear(100, 100), nn.ELU(),
    nn.Linear(100, 100), nn.ELU(),
    nn.Linear(100, 100), nn.ELU(),
    nn.Linear(100, 30), nn.ELU(),
    nn.Linear(30, num_meta),
    nn.Softmax(dim=1)
)

from copy import deepcopy
lobe_timelagged = deepcopy(lobe).to(device=device)
lobe = lobe.to(device=device)
print(lobe)


vampnet = VAMPNet(lobe=lobe, lobe_timelagged=lobe_timelagged, learning_rate=5e-4, device=device)
loader_train = DataLoader(train_data, batch_size=10000, shuffle=True)
loader_val = DataLoader(val_data, batch_size=len(val_data), shuffle=False)

model = vampnet.fit(loader_train, n_epochs=40,validation_loader=loader_val, progress=tqdm).fetch_model()
state_prob = model.transform(totdist_new)
pickle.dump(state_prob,open(f'Dual_CYC_prob_{num_meta}.pkl','wb'))


Inac_distances = np.load('./Sys3A_HMass_Distances.npy')
Ac_distances = np.load('./Sys3B_HMass_Distances.npy')

Inac_prob = model.transform(Inac_distances)
Ac_prob = model.transform(Ac_distances)

pickle.dump(Inac_prob,open(f'Dual_CYC_prob_Inac_{num_meta}.pkl','wb'))
pickle.dump(Ac_prob,open(f'Dual_CYC_prob_Ac_{num_meta}.pkl','wb'))



pickle.dump(vampnet.train_scores,open(f'Dual_CYC_training_score_{num_meta}.pkl','wb'))

pickle.dump(vampnet.validation_scores,open(f'Dual_CYC_val_score_{num_meta}.pkl','wb'))

pickle.dump(model, open(f'./Dual_Dual_CYC_model_{num_meta}.pkl','wb'))
