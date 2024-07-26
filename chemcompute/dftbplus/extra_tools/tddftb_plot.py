#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import chemcompute.common as common

data = np.loadtxt('excitation_ev.dat')
data_nm = np.loadtxt('excitation_nm.dat')


with PdfPages('UV-Vis_TD-DFTB_plot.pdf') as pdf:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Metadata informations
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    d = pdf.infodict()
    d['Title'] = ''
    d['Author'] = 'A. TETENOIRE'


    """
    PLOT
    """

    print('\n Plotting with various width for gaussian broadening')
    # Plot

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)

    for width in [0.05, 0.1, 0.2, 0.5]:
        pm_spectra = 0.5 # eV
        x_min, x_max = np.min(data[:, 0]) - pm_spectra, np.max(data[:, 0]) + pm_spectra
        x = np.arange(x_min, x_max, 0.01)


        spectra = np.zeros(len(x))
        for num ,value in enumerate(data):
            spectra += common.gaussian(x, value[1], value[0], width)
        ax.plot(x, spectra, linewidth=2, label=str('width=%seV' % width), alpha=0.75)




    # for vib in vibrations[i]:
    #     ax.vlines(vib, 0, 200, linewidth=1, color='k')

    # Parameters
    # ax.xaxis.set_ticks([1, 2, 3, 4])
    # ax.set_ylim(-6, -1)
    # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
    # ax.yaxis.set_ticks(np.arange(-6, 0, 1))

    # ax.set_xlim(0, threshold)
    # ax.set_ylim(0, 20000)

    # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
    # ax.yaxis.set_ticks(np.arange(0, 7, 1))

    ax.tick_params(axis='both', which='major', length=5, width=2)
    ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    ax.tick_params(axis='both', labelsize=16)
    ax.minorticks_on()
    # ax.tick_params(axis='x', which='minor', bottom=False)


    # ax.tick_params(axis='both', labelsize=16)
    # ax.tick_params(axis='both', which='major', length=5, width=2)
    # ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    # ax.yaxis.set_ticks_position('both')
    # ax.minorticks_on()

    ax.set_xlabel('frequency (eV)', fontsize=20)
    ax.set_ylabel('absorbance (a.u.)', fontsize=20)

    # ax.legend(fontsize=10, ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.15), frameon=False,  labelspacing=0.2, handletextpad=0.2, columnspacing=1)   
    # ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(0.9, 1), frameon=False)


    ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()



    """
    PLOT
    """


    # Plot

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)


    for width in [1, 5, 10, 20]:

        pm_spectra_nm = 50 # nm
        x_min_nm, x_max_nm = np.min(data_nm[:, 0]) - pm_spectra_nm, np.max(data_nm[:, 0]) + pm_spectra_nm
        x_nm = np.arange(x_min_nm, x_max_nm, 1)

        spectra_nm = np.zeros(len(x_nm))
        for num ,value in enumerate(data_nm):
            spectra_nm += common.gaussian(x_nm, value[1], value[0], width)
        ax.plot(x_nm, spectra_nm, linewidth=2, label=str('width=%snm' % width), alpha=0.75)




    # for vib in vibrations[i]:
    #     ax.vlines(vib, 0, 200, linewidth=1, color='k')

    # Parameters
    # ax.xaxis.set_ticks([1, 2, 3, 4])
    # ax.set_ylim(-6, -1)
    # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
    # ax.yaxis.set_ticks(np.arange(-6, 0, 1))

    # ax.set_xlim(0, threshold)
    # ax.set_ylim(0, 20000)

    # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
    # ax.yaxis.set_ticks(np.arange(0, 7, 1))

    ax.tick_params(axis='both', which='major', length=5, width=2)
    ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    ax.tick_params(axis='both', labelsize=16)
    ax.minorticks_on()
    # ax.tick_params(axis='x', which='minor', bottom=False)


    # ax.tick_params(axis='both', labelsize=16)
    # ax.tick_params(axis='both', which='major', length=5, width=2)
    # ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    # ax.yaxis.set_ticks_position('both')
    # ax.minorticks_on()

    ax.set_xlabel('wavelength (nm)', fontsize=20)
    ax.set_ylabel('absorbance (a.u.)', fontsize=20)

    # ax.legend(fontsize=10, ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.15), frameon=False,  labelspacing=0.2, handletextpad=0.2, columnspacing=1)   
    # ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(0.9, 1), frameon=False)


    ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()



    """
    PLOT
    """


    # Plot


    print('\n Plotting them in separated canvas')
    for width in [1, 5, 10, 20]:

        fig=plt.figure(figsize=(10,6), dpi=600)
        ax = fig.add_subplot(111)

        # plot periodic
        pm_spectra_nm = 50 # nm
        x_min_nm, x_max_nm = np.min(data_nm[:, 0]) - pm_spectra_nm, np.max(data_nm[:, 0]) + pm_spectra_nm
        x_nm = np.arange(x_min_nm, x_max_nm, 1)

        spectra_nm = np.zeros(len(x_nm))
        for num ,value in enumerate(data_nm):
            spectra_nm += common.gaussian(x_nm, value[1], value[0], width)
        ax.plot(x_nm, spectra_nm, linewidth=2, label=str('width=%snm-periodic' % width), alpha=0.75)


        # for vib in vibrations[i]:
        #     ax.vlines(vib, 0, 200, linewidth=1, color='k')

        # Parameters
        # ax.xaxis.set_ticks([1, 2, 3, 4])
        # ax.set_ylim(-6, -1)
        # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
        # ax.yaxis.set_ticks(np.arange(-6, 0, 1))

        # ax.set_xlim(0, threshold)
        # ax.set_ylim(0, 20000)

        # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
        # ax.yaxis.set_ticks(np.arange(0, 7, 1))

        ax.tick_params(axis='both', which='major', length=5, width=2)
        ax.tick_params(axis='both', which='minor', length=2.5, width=1)

        # ax.xaxis.set_ticks_position('both')
        ax.tick_params(axis='both', labelsize=16)
        ax.minorticks_on()
        # ax.tick_params(axis='x', which='minor', bottom=False)


        # ax.tick_params(axis='both', labelsize=16)
        # ax.tick_params(axis='both', which='major', length=5, width=2)
        # ax.tick_params(axis='both', which='minor', length=2.5, width=1)

        # ax.xaxis.set_ticks_position('both')
        # ax.yaxis.set_ticks_position('both')
        # ax.minorticks_on()

        ax.set_xlabel('wavelength (nm)', fontsize=20)
        ax.set_ylabel('absorbance (a.u.)', fontsize=20)

        # ax.legend(fontsize=10, ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.15), frameon=False,  labelspacing=0.2, handletextpad=0.2, columnspacing=1)   
        # ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(0.9, 1), frameon=False)


        ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

        


        pdf.savefig(bbox_inches='tight')
        plt.close()
