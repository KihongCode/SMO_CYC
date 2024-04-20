#Inactive -> Active
import pyemma.plots as mplt
import pyemma.msm as pyemmamsm
import numpy as np
import pickle
import pyemma

# Loading dtrajs
dtrajs = pickle.load(open('./Dtraj_Weights/clus_tica_dtrajs_400_50.pkl', 'rb'))

# Using Maximum Likelihood MSM
msm = pyemma.msm.estimate_markov_model(dtrajs, lag=300)

# Lists of values for sets A and B
A = []
B = []

tpt = pyemmamsm.tpt(msm, A, B).mfpt
