#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import numpy as np
# import modules
# import vaspfric as vfric
import sys
import os.path
import dftbplustools
import chemcompute.common as common
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


"""
Use to analyse the AMS-Raman calculation from dftb software.
ipython analysis_raman_calculation.py output_file_from_dftb
"""

# Checks
try:
    file = sys.argv[1]
except:
    print("!! Specify the file from which you want to extract dftb modes !!\n")
    sys.exit()

if not os.path.isfile(file):
    print('!! The input is not a file !!|n')
    sys.exit()



# Extract data from the file
dftb = dftbplustools.dftb_load_modes_out(file)
dftb_spectra = common.sum_gaussian(range(4000), dftb, 10, column=2)

# Save data for plot in clumn file
np.savetxt('data_raman_spectrum_gb-10.dat', dftb_spectra)





print('\nPlot Raman spectra:\t%s\n' % file)
with PdfPages('raman_spectrum.pdf') as pdf:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Metadata informations
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    d = pdf.infodict()
    d['Title'] = ''
    d['Author'] = 'A. TETENOIRE'


    """
    PLOT
    """

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)
    
    ax.plot(range(4000), dftb_spectra)
    for mode in dftb.values():
        ax.vlines(mode[0], 0, mode[1], color='black', linewidth=1)


    ax.tick_params(axis='both', which='major', length=5, width=2)
    ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    ax.tick_params(axis='both', labelsize=16)
    ax.minorticks_on()
    # ax.tick_params(axis='x', which='minor', bottom=False)



    ax.set_xlabel('wavenumer (cm-1)', fontsize=20)
    ax.set_ylabel(r'intensities (A$^{4}$/amu)', fontsize=20)


    pdf.savefig(bbox_inches='tight')
    plt.close()


    """
    PLOT
    """

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)
    
    ax.plot(range(4000), dftb_spectra / np.max(dftb_spectra))
    for mode in dftb.values():
        ax.vlines(mode[0], 0, mode[1] / np.max(dftb_spectra), color='black', linewidth=1)


    ax.set_ylim(-0.1, 1.1)

    ax.tick_params(axis='both', which='major', length=5, width=2)
    ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    ax.tick_params(axis='both', labelsize=16)
    ax.minorticks_on()
    # ax.tick_params(axis='x', which='minor', bottom=False)

    ax.set_xlabel('wavenumer (cm-1)', fontsize=20)
    ax.set_ylabel('intensities (a.u.)', fontsize=20)

    pdf.savefig(bbox_inches='tight')
    plt.close()


    """
    PLOT
    """
    for limits in [(0, 1050), (1000, 2050), (2000, 3050), (3000, 4000)]:

        fig=plt.figure(figsize=(10,6), dpi=600)
        ax = fig.add_subplot(111)
        
        ax.plot(range(4000), dftb_spectra / np.max(dftb_spectra))
        for mode in dftb.values():
            ax.vlines(mode[0], 0, mode[1] / np.max(dftb_spectra), color='black', linewidth=1)



        ax.set_xlim(limits[0], limits[1])
        ymax = max(list(dftb_spectra / np.max(dftb_spectra))[limits[0]:limits[1]])
        ymin = 0.1 * ymax
        ax.set_ylim(-ymin, ymax)

        ax.tick_params(axis='both', which='major', length=5, width=2)
        ax.tick_params(axis='both', which='minor', length=2.5, width=1)

        # ax.xaxis.set_ticks_position('both')
        ax.tick_params(axis='both', labelsize=16)
        ax.minorticks_on()
        # ax.tick_params(axis='x', which='minor', bottom=False)


        ax.set_xlabel('wavenumer (cm-1)', fontsize=20)
        ax.set_ylabel('intensities (a.u.)', fontsize=20)

        pdf.savefig(bbox_inches='tight')
        plt.close()
