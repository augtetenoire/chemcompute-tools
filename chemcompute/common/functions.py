from scipy.signal import argrelextrema
import numpy as np
from scipy.optimize import curve_fit



def maximum_location(x, y):
    #return the x,y values of the maximum ot the inputs

    m_y = np.max(y)
    temp = np.where(np.isclose(y, m_y))
    m_x = x[temp[0]]
    return m_x[0], m_y


def maximas_location(x, y):
    # return the sorted list of all the maximum of the inputs

    pic_max_index = argrelextrema(y, np.greater)[0]
    pic_max_y = [y[k] for k in pic_max_index]
    # Arrange all maxima to be from the highest to the lowest
    L = sorted(((i, j) for i, j in zip(pic_max_y, pic_max_index)), reverse=True)
    pic_max_y, pic_max_index = zip(*L)
    pic_max_index, pic_max_y = np.asarray(pic_max_index), np.asarray(pic_max_y)

    pic_max_x = [x[k] for k in pic_max_index]

    return list(pic_max_x), list(pic_max_y)




def gaussian(x, a, b, c):
    # x must be the list on x position where to evaluate the gaussian
    # a = height
    # b = position
    # c = width


    # Test if x is a list or array. If yes, return the gaussian evaluated in the full x range
    if hasattr(x, "__len__"):
        return np.asarray([a * np.exp(- (i - b)**2 / (2 * c**2)) for i in x])
    # If no, return the gaussian evaluated at the scalar x
    else:
        return a * np.exp((-(x - b)**2) / (2 * c**2))
    

def gaussian_fit(x, y):
    try:
        popt, pcov = curve_fit(gaussian, range(len(y)), y)
        popt[1] = popt[1] + np.min(x)
    except RuntimeError:
        popt = np.asarray([0, 1, 1])
    return popt


def sum_gaussian(range_def, dict_a, width, threshold=0, column=2):
    """
    Column = 2 is done to load the raman data of the spectra by default. If you change to 1, you load the IR data.
    """
    # range_def is the range in which you calculate the gaussian
    # dict_a is of the forn of "dftb_load_modes_out" function
    # width in the the width og the gaussian
    # threshold is use to get rid of the ferquencies that have veery small value. By default it is unset. With threshold=1, all vibrations that are below this value in intensity are skipped
    plot = np.zeros(len(range_def))
    for key in dict_a.keys():
        if threshold > 0 :
            if dict_a[key][0] > 0:
                if dict_a[key][2] > threshold:
                    plot += gaussian(range_def, dict_a[key][column], dict_a[key][0], width)
        else:
            plot += gaussian(range_def, dict_a[key][column], dict_a[key][0], width)
    return plot    


