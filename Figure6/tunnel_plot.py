import numpy as np
import matplotlib.pyplot as plt
import tol_colors as tc
from pdb3 import lsext
import mplhelv
from tqdm.notebook import tqdm
tol_cmap = tc.tol_cmap('rainbow_PuBr')
import pickle
from free_energy_plot import free_energy_plot, gap



l = free_energy_plot(d_Active,-z_Active,vmax=7)#, weightsClassA=weights)
l[1].set_xlabel('Diameter (Å)',fontsize=20)
l[1].set_ylabel('Z - Coordinate (Å)',fontsize=20)
l[1].set_ylim(-40,40)
yticks = range(-40,41,20)
l[1].set_yticks(yticks)
l[1].legend(fontsize=20,frameon=False)
#l[1].set_title('Cyclopamine bound to CRD', fontsize = 22)
l[0].savefig('/home/pdb3/kihongk2/Images/System82_Tunnel_Active.png',transparent=True,dpi=300)
