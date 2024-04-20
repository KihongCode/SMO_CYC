import numpy as np
import mdtraj as md
import os 


## Compute the 57 distances for all trajectories

for i in range(0,250):
	print(i)
	if os.path.exists(f'./npy/RUN0_CLONE{i}_Distances.npy'):
		continue
	try: 
        	t = md.load(f'./stripxtc/RUN0_CLONE{i}_strip.xtc',top='Sys3A_HMass_stripped.parm7')
	except OSError:
        	continue
	contacts = [[0, 1],[8,115],[27,75],\
                            [48,72],[50,51],[51,68],\
                            [55,61],[57,153],[59,148],\
                            [59,154],[61,65],[65,129],\
                            [93,105],[105,110],[111,116],\
                            [144,148],[148,153],[148,154],\
                            [149,150],[149,151],[164,457],\
                            [173,227],[173,232],[188,217],\
                            [194,201],[194,210],[198,210],\
                            [204,295],[226,232],[230,234],\
                            [232,233],[274,401],[277,281],\
                            [281,364],[281,391],[281,395],\
                            [281,477],[285,391],[288,387],\
                            [295,302],[298,302],[322,341],\
                            [323,334],[339,416],[339,419],\
                            [361,399],[375,376],[375,377],\
                            [377,378],[385,388],[412,416],\
                            [422,455],[429,433],[429,451],\
                            [444,446],[458,461],[476,479]]

	b = md.compute_contacts(t, contacts)
	np.save(f'./npy/RUN0_CLONE{i}_Distances.npy',b[0])


  ## Check that the distances correspond to the right residues
  
	contact_resis = [['PRO','PRO'],['ARG','ARG'],['TYR','LYS'],\
                ['LEU','TYR'],['LEU','TRP'],['TRP','LEU'],\
                ['ARG','TRP'],['ALA','GLU'],['ARG','TRP'],\
                ['ARG','GLY'],['TRP','GLN'],['GLN','PHE'],\
                ['ARG','TRP'],['TRP','ARG'],['CYS','PHE'],\
                ['ASN','TRP'],['TRP','GLU'],['TRP','GLY'],\
                ['TYR','GLU'],['TYR','ASP'],['PHE','LEU'],\
                ['HIS','PHE'],['HIS','ARG'],['LEU','PHE'],\
                ['PHE','SER'],['PHE','PHE'],['TRP','PHE'],\
                ['TYR','LEU'],['GLN','ARG'],['GLY','GLU'],\
                ['ARG','ARG'],['PHE','ALA'],['LEU','TRP'],\
                ['TRP','GLY'],['TRP','MET'],['TRP','GLY'],\
                ['TRP','TRP'],['PHE','MET'],['LEU','ILE'],\
                ['LEU','PHE'],['LYS','PHE'],['GLN','TYR'],\
                ['VAL','VAL'],['TYR','PHE'],['TYR','GLN'],\
                ['LEU','PHE'],['HIS','PRO'],['HIS','GLY'],\
                ['GLY','LEU'],['SER','ASN'],['HIS','PHE'],\
                ['TRP','PRO'],['TYR','GLN'],['TYR','ILE'],\
                ['GLN','ILE'],['LEU','LYS'],['THR','TRP']]
	for j,k in zip(contacts[:],contact_resis):
    		confirm1 = t.topology.select(f'resid {j[0]} and resname {k[0]}')
    		confirm2 = t.topology.select(f'resid {j[1]} and resname {k[1]}')
    		if confirm1.size == 0 or confirm2.size == 0:
        		print(j,k)
