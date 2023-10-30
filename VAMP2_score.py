from deeptime.markov import TransitionCountEstimator
from deeptime.plots import plot_implied_timescales
from deeptime.util.validation import implied_timescales
import matplotlib.pyplot as plt
import pickle
import numpy as np
from tqdm import tqdm
import pyemma
from deeptime.decomposition import VAMP

cutoffs = [10,20,30,40,50]
clus = [100,150,200,250,300,350,400,450,500]

# Create an empty list to store the results
results = []

for ct in tqdm(cutoffs):
    for k in tqdm(clus):
        print(k, ct)
        dtrajs = pickle.load(open(f'../msm/clus_tica_dtrajs/clus_tica_dtrajs_{k}_{ct}.pkl', 'rb'))
        msm = pyemma.msm.estimate_markov_model(dtrajs, lag=300)
        vamp_avg = np.mean(msm.score_cv(dtrajs))
        print(vamp_avg)

        # Append the current k, ct, and vamp_avg values to the results list
        results.append({'k': k, 'ct': ct, 'vamp_avg': vamp_avg})

# Save the results to a file using pickle
with open('results.pkl', 'wb') as f:
    pickle.dump(results, f)
