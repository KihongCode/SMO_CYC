## compute additional distances that are of interest

import numpy as np
import mdtraj as md
import os

for i in range(0,250):
    print(i)
    if os.path.exists(f'./DREnpy/RUN6_CLONE{i}_Distances.npy'):
        continue
    try:
            t = md.load(f'./stripxtcp6/RUN6_CLONE{i}_strip_strip.xtc',top='./stripgenp/stripped.5L7D_CYC_Sys1_HMass_stripped.parm7')
    except OSError:
            continue

  ## 0th corresponds to D-R distance, 1st corresponds to W-M distance
  
    contacts = [[281,391],[342,415],[342,460],[415,460]]

    b = md.compute_contacts(t, contacts)
    np.save(f'./DREnpy/RUN6_CLONE{i}_Distances.npy',b[0])
