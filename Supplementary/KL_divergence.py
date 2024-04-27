from itertools import combinations
import numpy as np
import pickle
from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler

def kl_divergence(p, q):
    kl_div = 0
    for i in range(len(p)):
        if not(p[i] == 0 or q[i] == 0):
            kl_div += p[i] * np.log2(p[i]/q[i])
    return kl_div

def calc_kld(array1,array2):
    a = [list(pair) for pair in combinations(range(496), 2)]
    indexs = np.unique(a)
    print('Loading arrays...')
    inac_comb = np.load(array1)
    ac_comb = np.load(array2)
    inac_comb = np.array(inac_comb)
    ac_comb = np.array(ac_comb)
    print('''Loaded!
Now Normalizing...''')
    inac_comb_norm = np.zeros(inac_comb.shape)
    ac_comb_norm = np.zeros(ac_comb.shape)
    for p in tqdm(range(ac_comb.shape[1])):
        feat_ac = ac_comb[:,p]
        feat_norm_ac = (feat_ac - np.mean(feat_ac))/(np.std(feat_ac))
        ac_comb_norm[:,p] = feat_norm_ac
        feat_inac = inac_comb[:,p]
        feat_norm_inac = (feat_inac - np.mean(feat_inac))/(np.std(feat_inac))
        inac_comb_norm[:,p] = feat_norm_inac
    del ac_comb
    del inac_comb
    number_of_feature = ac_comb_norm.shape[1]
    kl_avg = np.empty([number_of_feature,1])
    arr_shape = min(ac_comb_norm.shape[0],inac_comb_norm.shape[0])
    print('''Normalized!! 
Now Calculating kld''')
    for i in tqdm(range(number_of_feature)):
        y_data = ac_comb_norm[:arr_shape,i]
        x_data = inac_comb_norm[:arr_shape,i]
        minimum = np.min(np.minimum(x_data,y_data))
        maximum = np.max(np.maximum(x_data,y_data))
        bins = np.arange(minimum,maximum,(maximum-minimum)/100)
        xhist,xedges = np.histogram(x_data,bins=bins,density=True)
        yhist,yedges = np.histogram(y_data,bins=bins,density=True)
        x_prob = xhist * np.diff(xedges)
        y_prob = yhist * np.diff(yedges)
        kl_avg[i,0] = (kl_divergence(x_prob,y_prob) + kl_divergence(y_prob,x_prob))/2
    del inac_comb_norm
    del ac_comb_norm
    np.save(f'kl_avg_score_Active_Intermediate_norm.npy',kl_avg)
    kl_div = np.load(f'kl_avg_score_Active_Intermediate_norm.npy')
    weights_per_residue = np.empty([len(indexs),1])
    for i in range(len(indexs)):
        position = np.where(a==indexs[i])[0]
        weights_per_residue[i,0] = np.sum(kl_div[position])
    min_max_scaler = MinMaxScaler()
    weights_per_residue = min_max_scaler.fit_transform(weights_per_residue)
    indexes_sort = np.argsort(weights_per_residue)
    f = open(f'bound_ensemble_score_Active_Intermediate.pml','w')
    for i in range(len(weights_per_residue)):
        f.write('alter resi '+str(indexs[i]+1)+',' 'b = ' + str(weights_per_residue[i,0]) + '\n')
    f.close()


calc_kld('./Active/KL_Active_Distances_Merged.npy','./Intermediate/KL_Intermediate_Distances_Merged.npy')
