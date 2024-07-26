#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


file = 'EXC.DAT'
data = np.loadtxt(file, skiprows=5, usecols=(0,1))

np.savetxt('excitation_ev.dat', data)

data_nm = data.copy()
data_nm[:, 0] = np.asarray([1239.8 / i for i in data[:, 0]]) 

np.savetxt('excitation_nm.dat', data_nm)
