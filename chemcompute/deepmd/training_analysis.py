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
    ax.scatter(lcurve[:, 0], lcurve[:, 1], s=15, linewidth=0.5, marker='+', alpha=0.9, label='loss-validation', c='red')
    ax.scatter(lcurve[:, 0], lcurve[:, 2], s=15, linewidth=0.5, marker='+', alpha=0.9, label='loss-training', c='orange')
    # Energy RMSE
    ax.scatter(lcurve[:, 0], lcurve[:, 3], s=15, linewidth=0.5, marker='+', alpha=0.9, label='energy-validation', c='green')
    ax.scatter(lcurve[:, 0], lcurve[:, 4], s=15, linewidth=0.5, marker='+', alpha=0.9, label='energy-training', c='lime')
    # Force RMSE
    ax.scatter(lcurve[:, 0], lcurve[:, 5], s=15, linewidth=0.5, marker='+', alpha=0.9, label='force-validation', c='blue')
    ax.scatter(lcurve[:, 0], lcurve[:, 6], s=15, linewidth=0.5, marker='+', alpha=0.9, label='force-training', c='cyan')


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


    ax.legend(fontsize=10, loc='lower center', markerscale=3, bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()


    """
    PLOT
    """


    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)


    ax.scatter(lcurve[:, 0], lcurve[:, 1], s=10, linewidth=0.5, marker='+', label='validation set', c='red')
    ax.scatter(lcurve[:, 0], lcurve[:, 2], s=10, linewidth=0.5, marker='+', label='training set', c='orange')


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


    ax.legend(fontsize=10, loc='lower center', markerscale=3, bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()



    """
    PLOT
    """


    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)


    ax.scatter(lcurve[:, 0], lcurve[:, 3], s=15, linewidth=0.5, marker='+', alpha=0.9, label='energy-validation', c='green')
    ax.scatter(lcurve[:, 0], lcurve[:, 4], s=15, linewidth=0.5, marker='+', alpha=0.9, label='energy-training', c='lime')


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


    ax.legend(fontsize=10, loc='lower center', markerscale=3, bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()




    """
    PLOT
    """


    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)


    ax.scatter(lcurve[:, 0], lcurve[:, 5], s=15, linewidth=0.5, marker='+', alpha=0.9, label='force-validation', c='blue')
    ax.scatter(lcurve[:, 0], lcurve[:, 6], s=15, linewidth=0.5, marker='+', alpha=0.9, label='force-training', c='cyan')


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


    ax.legend(fontsize=10, loc='lower center', markerscale=3, bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()

