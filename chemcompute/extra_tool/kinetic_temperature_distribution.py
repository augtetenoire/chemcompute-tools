#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

#/home/auguste/Temporary_python/Summary_02_07_19/ekin_oszicar.dat


def test_ln(Nb, Temp, T):
    N = Nb
    kb = 1.381e-23  # J.K-1 --or-- m2.kg.s-2.K-1
    _beta_ = 1 / (kb * Temp)
    if (N % 2 == 0):
        A = 3 / 2 * N
        gamma = math.log(math.factorial(A-1))
        # print('A=\t', A)
        return A*(math.log(_beta_)-(_beta_*kb*T))+(A-1)*(math.log(A*kb*T))-gamma+math.log(3*N*kb/2)
    else:
        A = 3 / 2 * N
        B = A - 1 / 2
        gamma = math.log((math.factorial(2 * B) / (4 ** B * math.factorial(B))) * math.sqrt(math.pi))
        # print('B=\t', B)
        return A*(math.log(_beta_)-(_beta_*kb*T))+(A-1)*(math.log(A*kb*T))-gamma+math.log(3*N*kb/2)


kinetic_energy_path = str(input("Enter the Path to the kinetic energy file:\n"))
number_atom = int(input("Enter the number of atom considered in the kinetic energy (integer):\n"))
ideal_temperature = float(input("Enter the ideal temperature (integer):\n"))

kinetic_temperature = np.loadtxt(fname=kinetic_energy_path)[:, 1]*2*1.602*10**(-19)/(3*number_atom*1.381*10**(-23))
tmin = int(np.min(kinetic_temperature))
tmax = int(np.max(kinetic_temperature))
_T_ = np.arange(tmin, tmax)

_dist_ = np.asarray([math.exp(test_ln(number_atom, ideal_temperature, i)) for i in _T_])

plt.hist(kinetic_temperature, bins='auto', density=True, label='Normalized distribution of temperature.\nT(mean)=%s' % round(np.mean(kinetic_temperature), 3))

plt.plot(_T_, _dist_, label='Maxwell-Boltzmann distribution.\nT=%s,N=%s' % (ideal_temperature, number_atom))
plt.xlabel('Temperature (K)')
plt.ylabel('Quantity (a.u.)')
plt.title('Normalized distribution of temperature of the system')
plt.legend(loc=1, fontsize='x-small')
fig = plt.gcf()
fig.savefig('temperature_distribution.pdf')
plt.show()
