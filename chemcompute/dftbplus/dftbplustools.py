import numpy as np


def dftb_load_modes_out(file):
    # np.asarray(list(a.values()))[:, 0] to get the values as array
    with open(file, 'r') as foo:
        llines = foo.readlines()
    load = False
    dmodes = {}
    for line in llines:
        if len(line.split()) > 0:
            if load:
                if '-' in line.split()[0]:
                    dmodes[int(line.split('-')[0])] = np.asarray([0, 0, 0])
                else:
                    # If the mode has IR and raman value is does load them also
                    dmodes[int(line.split()[0])] = np.asarray([float(x) for x in line.split()[1:]])
            if line.split()[0] == 'Mode':
                load = True
    return dmodes
