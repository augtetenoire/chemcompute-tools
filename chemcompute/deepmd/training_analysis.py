#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# from dpdata import LabeledSystem, MultiSystems
# import dpdata
# import glob

lcurve = np.loadtxt('lcurve.out', skiprows=1)

with PdfPages('training_analysis.pdf') as pdf:
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

    # Loss
    ax.plot(lcurve[:, 0], lcurve[:, 1], label='loss-validation', color='red')
    ax.plot(lcurve[:, 0], lcurve[:, 2], label='loss-training', color='orange')
    # Energy RMSE
    ax.plot(lcurve[:, 0], lcurve[:, 3], label='energy-validation', color='green')
    ax.plot(lcurve[:, 0], lcurve[:, 4], label='energy-training', color='lime')
    # Force RMSE
    ax.plot(lcurve[:, 0], lcurve[:, 5], label='force-validation', color='blue')
    ax.plot(lcurve[:, 0], lcurve[:, 6], label='force-training', color='cyan')


    # Parameters

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

    ax.set_yscale('log')

    ax.set_xlabel('Steps (count)', fontsize=20)
    ax.set_ylabel('Loss function', fontsize=20)


    ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()


    """
    PLOT
    """


    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)


    ax.plot(lcurve[:, 0], lcurve[:, 1], label='validation set', color='red')
    ax.plot(lcurve[:, 0], lcurve[:, 2], label='training set', color='orange')


    # Parameters

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

    ax.set_yscale('log')

    ax.set_xlabel('Steps (count)', fontsize=20)
    ax.set_ylabel('Loss function', fontsize=20)


    ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()



    """
    PLOT
    """


    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)


    ax.plot(lcurve[:, 0], lcurve[:, 3], label='validation set', color='green')
    ax.plot(lcurve[:, 0], lcurve[:, 4], label='training set', color='lime')


    # Parameters

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

    ax.set_yscale('log')

    ax.set_xlabel('Steps (count)', fontsize=20)
    ax.set_ylabel('Energy RMSE (eV)', fontsize=20)


    ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()




    """
    PLOT
    """


    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)


    ax.plot(lcurve[:, 0], lcurve[:, 5], label='validation set', color='blue')
    ax.plot(lcurve[:, 0], lcurve[:, 6], label='training set', color='cyan')


    # Parameters

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

    ax.set_yscale('log')

    ax.set_xlabel('Steps (count)', fontsize=20)
    ax.set_ylabel(r'Force RMSE (eV/$\AA^{2}$)', fontsize=20)


    ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()
