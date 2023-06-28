def gaussian_func(x,*params):
    """ generate the Gaussian distribution
    Args:
        x(array): the chain lengths
        params[list]: [amplitude,mean,standard deviation] parameters required for generating the Gaussian distribution
    returns:
        y(array): the distribution
    Note:
        if the length of params is more than 3, then we will have a mixture of Gaussian"""
    y = np.zeros_like(x)
    for i in range(0,len(params),3):
        amp= params[i] # amplitude
        ctr = params[i+1] # peak location
        wid = params[i+2] # standard deviation
        y += amp*np.exp(-((x-ctr)/wid)**2)
    return y
