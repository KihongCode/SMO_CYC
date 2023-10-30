import subprocess
from pdb3 import *
from natsort import natsorted
import mdtraj as md
from tqdm import tqdm

pdbs,npdbs = lsext('./Active_frames/','.pdb',preapp=True)
pdbs = natsorted(pdbs)
#print(pdbs)
def holescriptgen():
  for i,j in tqdm(enumerate(pdbs),total=len(pdbs)):
    t = md.load(j)
    atoms = ['CG1_350','OG1_408','CE_467']
    atomnos = [t.topology.select("name {} and resi {}".format(*j.split('_')))[0] for j in atoms]
    COM = md.compute_center_of_mass(t.atom_slice(atomnos))*10
    #print(*COM[0])
    COMp = ' '.join([str(round(j,4)) for j in COM[0]])
    f = open(f'./hole_input_Active/hole_msm_input_{i+1}.inp','w+')
    f.write(f'''coord {j}      ! Co-ordinates in pdb format
radius /home/kihongk2/hole/hole2/rad/simple.rad  ! Use simple AMBER vdw radii
                ! n.b. can use ~ in hole
!
! now optional cards
sphpdb /home/kihongk2/hole/82/sph_ac/hole_msm_input_{i+1}.sph      ! pdb format output of hole sphere centre info
cvect 0.0 0.0 1.0        ! channel runs in Z direction
cpoint {COMp}''')
    f.close()

holescriptgen()
