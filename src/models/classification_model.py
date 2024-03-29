import numpy as np
from sklearn.mixture import GaussianMixture





def classification_func(distribution,n_comps):
    """Identify subpopulations
    Args:
        distributions(df): columns =[chain_length,weight_fraction]
        n_comps(int): the number of clusters to identify
    returns:
        list: [weight, mean,standard deviation] of each cluster
    """
    # creating a model and fitting the model to the data
    gmm =GaussianMixture(n_components=n_comps, covariance_type='full').fit(distribution)
    mean = gmm.means_[:,0] # the first columns contains the means
    #covariance returns a set of arrays each for one cluster. The main diagonal contains the variance
    covariance = gmm.covariances_
    # the weights here are the population fractions
    weight = gmm.weights_

    cluster_parms =[] # to store the cluster parameters
    for i in range(n_comps):
        cluster_parms.append([weight[i],mean[i],np.sqrt(np.diag(covariance[i]))[0]])
    return list(np.hstack(cluster_parms))


