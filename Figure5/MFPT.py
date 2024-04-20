#Inactive -> Active
import pyemma.plots as mplt
import pyemma.msm as pyemmamsm
import numpy as np
import pickle
import pyemma

# Loading dtrajs
dtrajs = pickle.load(open('./Dtraj_Weights/clus_tica_dtrajs_150_40.pkl', 'rb'))

# Using Maximum Likelihood MSM
msmlove = pyemma.msm.estimate_markov_model(dtrajs, lag=300)

# Lists of values for sets A and B
A = [10,111]
B = [109,7]

tpt1 = pyemmamsm.tpt(msmlove, A, B).mfpt

A = [10]
B = [109]

tpt2 = pyemmamsm.tpt(msmlove, A, B).mfpt

A = [10,111]
B = [109,7]

tpt3 = pyemmamsm.tpt(msmlove, B, A).mfpt

A = [10]
B = [109]

tpt4 = pyemmamsm.tpt(msmlove, B, A).mfpt

import numpy as np

def calculate_stats(tpt1, tpt2):
    # Convert the inputs to numpy arrays
    tpt1 = np.array(tpt1)
    tpt2 = np.array(tpt2)
    
    # Calculate the standard deviation
    std_dev = np.std([tpt1, tpt2])
    
    # Calculate the average (mean)
    average = np.mean([tpt1, tpt2])
    
    return std_dev, average



std_dev, average = calculate_stats(tpt1, tpt2)
print(f"The standard deviation between tpt1 and tpt2 is: {std_dev}")
print(f"The average between tpt1 and tpt2 is: {average}")



def calculate_stats(tpt3, tpt4):
    # Convert the inputs to numpy arrays
    tpt3 = np.array(tpt3)
    tpt4 = np.array(tpt4)
    
    # Calculate the standard deviation
    std_dev = np.std([tpt3, tpt4])
    
    # Calculate the average (mean)
    average = np.mean([tpt3, tpt4])
    
    return std_dev, average


std_dev, average = calculate_stats(tpt3, tpt4)
print(f"The standard deviation between tpt3 and tpt4 is: {std_dev}")
print(f"The average between tpt3 and tpt4 is: {average}")
