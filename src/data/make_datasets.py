from sklearn.mixture import GaussianMixture


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


