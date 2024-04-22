import numpy as np
import numpy.linalg as la
import os
from natsort import natsorted
import matplotlib.pyplot as plt
import matplotlib as mpl
def lsext(path,ext,extra=None,sort=False,preapp=True,extranot=None,nat=True,pathcheck=False,abs=True,extraand=None):
    extens = [j for j in os.listdir(path) if '{}'.format(ext) in j]
    if extra != None:
        if isinstance(extra,str):
            extens = [j for j in extens if '{}'.format(extra) in j]
        elif isinstance(extra,list):
            extens2 = [j for j in extens if '{}'.format(extra[0]) in j]
            for extraelem in extra[1:]:
                extens2.extend([j for j in extens if '{}'.format(extraelem) in j])
            extens = extens2
    if extraand!=None:
        for extraelem in extraand:
            extens = [j for j in extens if f'{extraelem}' in j]
    if extranot != None:
        if isinstance(extranot,str):
            extens = [j for j in extens if '{}'.format(extranot) not in j]
        elif isinstance(extranot,list):
            extens2 = [j for j in extens if '{}'.format(extranot[0]) not in j]
            #print(len(extens),len(extens2))
            for extraelem in extranot[1:]:
                extens2 = [j for j in extens2 if '{}'.format(extraelem) not in j]
                #print(len(extens),len(extens))
            extens = extens2[:]
    if preapp:
        extens = [path+j for j in extens]
    if sort:
        extens=sorted(extens)
    if nat:
        extens=natsorted(extens)
    if pathcheck and preapp:
        extens = [j for j in extens if os.path.exists(j)]
    if abs and preapp:
        extens = [os.path.abspath(j) for j in extens]
    leng = len(extens)
    return (extens,leng)
