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
tol_cmap = tc.tol_cmap('rainbow_PuBr')

npys = lsext('./57npy_14942//','.npy')[0]+lsext('./57npy_14943/','.npy')[0]
total_data = []
for npy in tqdm(npys):
    y = np.load(npy)
    total_data.append(y)
    
print(len(total_data))

tica = TICA(lagtime=300, var_cutoff=95/100).fit_fetch(np.concatenate(total_data))

projection = [tica.transform(x) for x in total_data]

tica_concatenated = np.concatenate(projection)

pickle.dump(projection, open(f'./msm/tica_transformed/tica_transformed_data_65.pkl','wb'))
