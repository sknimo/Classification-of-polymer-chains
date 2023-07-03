# importing the required modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import models.classification_model as model
import utils.funcs as fn

#loading our file
fname ='../data/interim/chain_distribution.csv'
augmented_distribution = pd.read_csv(fname)
original_distro = pd.read_csv('../data/raw/Dataset.csv')


# Choosing the best number of clusters. We will loop over 6 clusters
# calculate the area under the curve from the predictios from clustering and compare it to original data
# The number of clusters from which the error changes no more will be chosen

clusters_param = []
error = []
for n in range(1,6):
    predictions = model.classification_func(augmented_distribution,n_comps=n)
    optimized_parms = fn.optimization_routine(augmented_distribution, predictions,fn.gaussian_func)
    clusters_param.append(optimized_parms)
    # in determining the goodness of fit, the error will be calculated using the original data not the generated data
    area_org = np.trapz(x=original_distro.iloc[:,0],y=original_distro.iloc[:,1])
    area_gen = np.trapz(x=original_distro.iloc[:,0],y=fn.gaussian_func(original_distro.iloc[:,0],*optimized_parms))
    error.append(abs(area_org-area_gen))# checking the error# checking the error

error_df = pd.DataFrame({'n_comps':np.arange(1,6),'error':error})
error_df.to_csv('../data/processed/errors.csv', index=False)

# saving output
curve_dic = {}
n =1
# note a cluster contains more than 1 subpopulation and represent the entire distrib
for clusters in clusters_param:
    dist = []
    # adding the x-axis values
    dist.append(original_distro.iloc[:,0])
    dist.append(original_distro.iloc[:,1])
    # looping over each distribution in the clusters
    for curve in clusters:
        dist.append(fn.single_gauss(original_distro.iloc[:,0],curve))
    curve_dic[n] = dist
    n+=1

# saving output to file
with pd.ExcelWriter('../data/processed/distributions.xlsx') as writer:
    for key,val in curve_dic.items():
        # stacking the curves and storing them to a dataframe
        cols = [f'curve{i}' for i in range(1,len(val)-1)]
        cols = ['chain_length','original_population'] + cols
        df = pd.DataFrame(np.asarray(val).T)
        df.columns = cols
        df.head(n=2)
        df.to_excel(writer,sheet_name=f'nComps{key}',index=False)
