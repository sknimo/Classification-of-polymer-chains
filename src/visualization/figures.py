
plt.style.use('seaborn-dark')


def plot_distro(df):
    """Plots the deconvoluted distribution
    Args:
        df: is dataframe with the first column being the chain length and the remaining deconvoluted distro
    returns:
        None but sends plot to report folder"""

    fig = plt.figure(figsize=(4,3))


