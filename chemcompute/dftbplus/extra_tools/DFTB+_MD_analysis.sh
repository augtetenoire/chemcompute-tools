#/bin/bash

# A small script that plot standard analysis for MD run with DFTB+

grep 'Total Energy' output_dftb_MD_calculation_*.out |awk '{print $5}' > total_potential_energy.dat
grep 'MD Temperature' output_dftb_MD_calculation_*.out|awk '{print $5}' > md_temperature.dat


ipython << EOF

import numpy as np
from matplotlib import pyplot as plt
a = np.loadtxt('total_potential_energy.dat')
b = np.loadtxt('md_temperature.dat')
plt.plot(range(len(a)), (a[:]-a[0])) ; plt.xlabel('MD step (fs)') ; plt.ylabel('Potential energy (eV)') ;plt.savefig('potential_energy.png') ; plt.close()
plt.plot(range(len(a)), (a[:]-a[0])/(3*188*8.617e-5)*2, label='T=2E/3Nkb') ; plt.plot(range(len(b)), b[:], label='Md temperature') ; plt.xlabel('MD step (fs)') ; plt.ylabel('Temperature (K)') ;plt.savefig('temperature.png') ; plt.close()

EOF