import pandas as pd
from sklearn.mixture import GaussianMixture
# from openpyxl.workbook import Workbook

f_name = '../../data/raw/Dataset.csv'
raw_data = pd.read_csv(f_name)
def distribution_generation(raw_data):
    """Fit Gaussian model to data and use learning to generate reliable distribution
    Args:
        raw_data(array): [chain_length,weight_fraction]
    Returns:
        new_distro(array): learnt weight_fractions
    Note:
        The Gaussian mixture model is fitted 2X, because sometimes the first learning is not perfect"""
    for i in range(2):
        gmm_learning =GaussianMixture(n_components=len(raw_data), covariance_type='full').fit(raw_data.dropna().values)
    new_distro = gmm_learning.sample(1000)[0]
    return new_distro

# generating a more reliable dataset and storing it in interim folder
new_data = distribution_generation(raw_data)
new_dist = pd.DataFrame(new_data,columns=['chain_length','weight_fraction'])
new_dist.to_excel('../../data/interim/chain_distribution.xlsx',index=False)
