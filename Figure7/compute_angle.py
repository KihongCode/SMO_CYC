import numpy as np
import mdtraj as md
import os 




t = md.load(f'/home/pdb3/kihongk2/rf_try/simulation_data/var1/sim2.xtc',top='/home/pdb3/kihongk2/Cyclopamine_project/System2/production/PROD3/cpptraj_strip/stripped.Sys2_HMass.parm7')
topology = md.load_prmtop('/home/pdb3/kihongk2/Cyclopamine_project/System2/production/PROD3/cpptraj_strip/stripped.Sys2_HMass.parm7')
trajectory = md.load(f'/home/pdb3/kihongk2/rf_try/simulation_data/var1/sim2.xtc',top='/home/pdb3/kihongk2/Cyclopamine_project/System2/production/PROD3/cpptraj_strip/stripped.Sys2_HMass.parm7')

        
    
atom_indices = np.array([
    topology.select('resid 414 and name CA'),
    topology.select('resid 414 and name CB'),
    topology.select('resid 414 and name CG'),
    topology.select('resid 414 and name CD1')
])

atom_indices = atom_indices.reshape((-1, 4))
chi2_dihedral_Angles_82_Active = md.compute_dihedrals(trajectory, atom_indices)

np.save(f'./Angles_82_Active/Angles_82_Active9.npy',chi2_dihedral_Angles_82_Active)
