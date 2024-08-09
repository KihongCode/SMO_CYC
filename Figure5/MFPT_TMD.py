import pickle
import numpy as np
from tqdm import tqdm

inactive = [56,73,87]
intermediate = [145,30,60]
active = [29,57,53]

inactive_active = []
active_inactive = []
inactive_intermediate = []
intermediate_inactive = []
intermediate_active = []
active_intermediate = []

for i in tqdm(range(1, 201), desc="Processing files"):
    filename = f'/home/kihongk2/MSM_Construction/System19/msm/bt/msm_btsp_56_{i}.pkl'

    with open(filename, 'rb') as file:
        msm = pickle.load(file)

        mfpt_inactive_active = msm.mfpt(inactive, active)
        mfpt_active_inactive = msm.mfpt(active, inactive)
        mfpt_inactive_intermediate = msm.mfpt(inactive, intermediate)
        mfpt_intermediate_inactive = msm.mfpt(intermediate, inactive)
        mfpt_intermediate_active = msm.mfpt(intermediate, active)
        mfpt_active_intermediate = msm.mfpt(active, intermediate)

        inactive_active.append(mfpt_inactive_active)
        active_inactive.append(mfpt_active_inactive)
        inactive_intermediate.append(mfpt_inactive_intermediate)
        intermediate_inactive.append(mfpt_intermediate_inactive)
        intermediate_active.append(mfpt_intermediate_active)
        active_intermediate.append(mfpt_active_intermediate)

averages = {
    'inactive_active': np.mean(inactive_active),
    'active_inactive': np.mean(active_inactive),
    'inactive_intermediate': np.mean(inactive_intermediate),
    'intermediate_inactive': np.mean(intermediate_inactive),
    'intermediate_active': np.mean(intermediate_active),
    'active_intermediate': np.mean(active_intermediate)
}

std_devs = {
    'inactive_active': np.std(inactive_active),
    'active_inactive': np.std(active_inactive),
    'inactive_intermediate': np.std(inactive_intermediate),
    'intermediate_inactive': np.std(intermediate_inactive),
    'intermediate_active': np.std(intermediate_active),
    'active_intermediate': np.std(active_intermediate)
}

results = {
    'averages': averages,
    'std_devs': std_devs
}
with open('19_mfpt_averages_stddevs.pkl', 'wb') as f:
    pickle.dump(results, f)

print("Averages and standard deviations have been saved to '19_mfpt_averages_stddevs.pkl'")
