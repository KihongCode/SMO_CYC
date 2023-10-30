from deeptime.markov import TransitionCountEstimator
from deeptime.markov.msm import BayesianMSM
from deeptime.plots.chapman_kolmogorov import plot_ck_test
import pickle
import numpy as np
from tqdm import tqdm

models = []
lags=np.append(np.arange(10,300,10),np.arange(300,600,10))
for lag in tqdm(lags):
    msm28 = pickle.load(open(f'./bmsm/msmobjs/msmobj_400_50_{lag}.pkl','rb'))
    models.append(msm28)
test_model = models[29]
ck_test = test_model.ck_test(models, n_metastable_sets=5)
grid = plot_ck_test(ck_test, legend=True)
grid.figure.savefig('./CKTEST_3A3B_400_50.jpeg', transparent=False,dpi=300)
