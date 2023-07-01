


def gaussian_func(x,*params):
    """ generate the Gaussian distribution
    Args:
        x(array): the chain lengths
        params[list]: [amplitude,mean,standard deviation] parameters required for generating the Gaussian distribution
    returns:
        y(array): generated distribution
    Note:
        if the length of params is more than 3, then we will have a mixture of Gaussian"""
    y = np.zeros_like(x)
    # in case the output is made of arrays convert to list
    if type(params) == np.ndarray:
        params = np.concatenate(params).tolist()
    for i in range(0,len(params),3):
        amp= params[i] # amplitude
        ctr = params[i+1] # peak location
        wid = params[i+2] # standard deviation
        y += amp*np.exp(-((x-ctr)/wid)**2)
    return y

def optimization_routine(rawdata, gmm_parameters,gaussFunct):
    """Optimize parameters obtained from classification model
    Args:
        rawData(df): raw data
        gmm_parameters[list]: list of init parameters obtained from GMM
        gaussFunct(functions): gaussian functions to be used to perform curve optimization
    returns:
        array: [amp, peak location, width]
    """
    x_raw = rawdata.iloc[:,0].dropna().values;y_raw=rawdata.iloc[:,1].dropna().values

    # returns the fitting parameters, accepts the function,data and init_para
    popt_gauss, pcov_gauss = curve_fit(gaussFunct, x_raw, y_raw, p0=gmm_parameters, maxfev = 50000)


    optimizedParameter = np.asarray(popt_gauss).reshape(-1,3)
    return sorted(optimizedParameter, key= lambda x: x[1])

def single_gauss(x,params):
    """ Generates a single Gaussian curve
    Args:
        x(array): chain lenghts
        params(list): [amp,mean,std]
    returns:
        y(array): the Gaussian curve"""
    amp,ctr,wid= params[0],params[1],params[2]
    return amp*np.exp(-((x-ctr)/wid)**2)
