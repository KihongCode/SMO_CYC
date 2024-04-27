from deeptime.markov.msm import BayesianMSM
from deeptime.markov import TransitionCountEstimator
from deeptime.plots import plot_implied_timescales
from deeptime.util.validation import implied_timescales
import matplotlib.pyplot as plt
import pickle
import numpy as np
from tqdm import tqdm
lags=np.append(np.arange(10,300,10),np.arange(300,600,10))
models = []
for lag in tqdm(lags):
    dtrajs = pickle.load(open(f'../msm/clus_tica_dtrajs/clus_tica_dtrajs_150_40.pkl','rb'))
    count_model = TransitionCountEstimator(lag, 'effective').fit_fetch(dtrajs)
    bmsm = BayesianMSM().fit_fetch(count_model.submodel_largest())
    models.append(bmsm)
    pickle.dump(bmsm,open(f'../bmsm/msmobjs/msmobj_150_40_{lag}.pkl','wb'))
its_data = implied_timescales(models)
fig, ax = plt.subplots(1, 1)
plot_implied_timescales(its_data, n_its=2, ax=ax)
ax.set_yscale('log')
ax.set_title(f'Implied timescales, 150, 40')
ax.set_xlabel('lag time (steps)')
ax.set_ylabel('timescale (steps)')
fig.savefig(f'../bmsm/its/ITS_plot_150_40.jpg',dpi=300)
