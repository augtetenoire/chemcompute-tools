#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

    
lfiles = [
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr0/job_127175_calculation/hessian_calculations/job_131133_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131133.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr0/job_127175_calculation/hessian_calculations/job_131133_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131133.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr1_var1/job_127119_calculation/hessian_calculations/job_131935_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131935.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr1_var1/job_127119_calculation/hessian_calculations/job_131935_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131935.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr1_var2/job_127120_calculation/hessian_calculations/job_131135_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131135.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr1_var2/job_127120_calculation/hessian_calculations/job_131135_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131135.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr2_var1/job_127121_calculation/hessian_calculations/job_131136_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131136.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr2_var1/job_127121_calculation/hessian_calculations/job_131136_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131136.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr2_var2/job_127122_calculation/hessian_calculations/job_131137_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131137.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr2_var2/job_127122_calculation/hessian_calculations/job_131137_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131137.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr2_var3/job_127123_calculation/hessian_calculations/job_131138_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131138.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr2_var3/job_127123_calculation/hessian_calculations/job_131138_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131138.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr3_var1/job_127124_calculation/hessian_calculations/job_131139_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131139.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr3_var1/job_127124_calculation/hessian_calculations/job_131139_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131139.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr3_var2/job_127125_calculation/hessian_calculations/job_131140_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131140.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr3_var2/job_127125_calculation/hessian_calculations/job_131140_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131140.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr4/job_127126_calculation/hessian_calculations/job_131141_hessian_calculation/frozen_slab/modes_dftb_hessian_calculation_131141.out',
    '/Users/atetenoire/server/Au/gold_surface_calix_acid/Au_111_calix_acid/dftb/calix_adsorbed/different_anchors/anchr4/job_127126_calculation/hessian_calculations/job_131141_hessian_calculation/free_slab/modes_dftb_hessian_calculation_131141.out',
]

llabels = [
    'anchr0_frozen',
    'anchr0_free',
    'anchr1_var1_frozen',
    'anchr1_var1_free',
    'anchr1_var2_frozen',
    'anchr1_var2_free',
    'anchr2_var1_frozen',
    'anchr2_var1_free',
    'anchr2_var2_frozen',
    'anchr2_var2_free',
    'anchr2_var3_frozen',
    'anchr2_var3_free',
    'anchr3_var1_frozen',
    'anchr3_var1_free',
    'anchr3_var2_frozen',
    'anchr3_var2_free',
    'anchr4_frozen',
    'anchr4_free',
]



lmarkers = [
    '|'
] * len(llabels)


dcolors = {
    'red': "#FF0000",
    'blue': "#0000FF",
    'orange': "#FF8800",
    'turquoise': "#00FFFF",
    'black': "#000000",
    'grey': "#666666",
    'yellow': "#FFAA00",
    'green': "#00C11A",
    'pink': "#FF00EE",
    'dred': "#880000",
    'dgreen': "#008800",
    'dblue': "#000088",
    'violet': "#880088",
    'dyellow': "#888800",
    'dturquoise': "#008888",
    'blue2': "#8800FF",
    'green2': "#88FF00",
    'pink2': "#FF0088",
    'lgreen': "#00FF88",
    'lblue': "#0088FF",
}
lcolors = [i for i in dcolors.values()] * 2


# load the modes in the files
dall_modes = {}
for num, file in enumerate(lfiles):
    with open(file, 'r') as foo:
        llines = foo.readlines()
    load = False
    dmodes = {}
    for line in llines:
        if len(line.split()) > 0:
            if load:
                # If the mode has IR and raman value is does load them also
                dmodes[int(line.split()[0])] = np.asarray([float(x) for x in line.split()[1:]])
            if line.split()[0] == 'Mode':
                load = True
    dall_modes[llabels[num]] = dmodes






def plot_energy(labels, x, y, marker, xlabel, ylabel, lcolors):

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)

    labels = list(labels)

    # Plot
    for i in range(len(labels)):
        ax.scatter(x[i], [y[i]] * len(x[i]), s=40, label=labels[i], color=lcolors[i], marker=marker[i])

    # Parameters
    # ax.xaxis.set_ticks([1, 2, 3, 4])
    # ax.set_ylim(-6, -1)
    # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
    # ax.yaxis.set_ticks(np.arange(-6, 0, 1))

    # ax.set_xlim(0, 4.05)
    # ax.set_ylim(0, 6)

    # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
    # ax.yaxis.set_ticks(np.arange(0, 7, 1))

    ax.tick_params(axis='both', which='major', length=5, width=2)
    ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    ax.tick_params(axis='both', labelsize=16)
    ax.minorticks_on()
    ax.tick_params(axis='x', which='minor', bottom=False)


    # ax.tick_params(axis='both', labelsize=16)
    # ax.tick_params(axis='both', which='major', length=5, width=2)
    # ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    # ax.yaxis.set_ticks_position('both')
    # ax.minorticks_on()

    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)

    # ax.legend(fontsize=10, ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.15), frameon=False,  labelspacing=0.2, handletextpad=0.2, columnspacing=1)   
    # ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(0.9, 1), frameon=False)


    ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

   


def plot_energy_windowed(labels, x, y, marker, xlabel, ylabel, lcolors):

    w = [
        [0, 1000],
        [1000, 2000],
        [2000, 3000],
        [3000, 4000]
    ]

    for window in w:
        fig=plt.figure(figsize=(10,6), dpi=600)
        ax = fig.add_subplot(111)

        labels = list(labels)

        # Plot
        for i in range(len(labels)):
            ax.scatter(x[i], [y[i]] * len(x[i]), s=40, label=labels[i], color=lcolors[i], marker=marker[i])

        # Parameters
        # ax.xaxis.set_ticks([1, 2, 3, 4])
        # ax.set_ylim(-6, -1)
        # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
        # ax.yaxis.set_ticks(np.arange(-6, 0, 1))

        ax.set_xlim(window[0], window[1])
        # ax.set_ylim(0, 6)

        # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
        # ax.yaxis.set_ticks(np.arange(0, 7, 1))

        ax.tick_params(axis='both', which='major', length=5, width=2)
        ax.tick_params(axis='both', which='minor', length=2.5, width=1)

        # ax.xaxis.set_ticks_position('both')
        ax.tick_params(axis='both', labelsize=16)
        ax.minorticks_on()
        ax.tick_params(axis='x', which='minor', bottom=False)


        # ax.tick_params(axis='both', labelsize=16)
        # ax.tick_params(axis='both', which='major', length=5, width=2)
        # ax.tick_params(axis='both', which='minor', length=2.5, width=1)

        # ax.xaxis.set_ticks_position('both')
        # ax.yaxis.set_ticks_position('both')
        # ax.minorticks_on()

        ax.set_xlabel(xlabel, fontsize=20)
        ax.set_ylabel(ylabel, fontsize=20)

        # ax.legend(fontsize=10, ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.15), frameon=False,  labelspacing=0.2, handletextpad=0.2, columnspacing=1)   
        # ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(0.9, 1), frameon=False)


        ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

        pdf.savefig(bbox_inches='tight')
        plt.close()


with PdfPages('vibrational_modes.pdf') as pdf:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Metadata informations
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    d = pdf.infodict()
    d['Title'] = ''
    d['Author'] = 'A. TETENOIRE'

 
    '''
    All
    '''

    # labels = llabels[0:2]
    # x_pos = [np.asarray(list(dall_modes[llabels[0]].values())), np.asarray(list(dall_modes[llabels[1]].values()))]
    # y_pos = [0, 1]
    # markers = lmarkers
    # colors = lcolors

    # plot_energy(labels=labels, x=x_pos, y=y_pos, marker=markers,  xlabel=r'vibrational frequency (cm$^{-1}$)', ylabel='different calculations', lcolors=colors)
    
    # pdf.savefig(bbox_inches='tight')
    # plt.close()

    '''
    All
    '''

    labels = llabels
    x_pos = [np.asarray(list(dall_modes[llabels[x]].values())) for x in range(18)]
    y_pos = np.arange(0, 4, 0.2)
    markers = lmarkers
    colors = lcolors

    plot_energy(labels=labels, x=x_pos, y=y_pos, marker=markers,  xlabel=r'vibrational frequency (cm$^{-1}$)', ylabel='different calculations', lcolors=colors)
    
    pdf.savefig(bbox_inches='tight')
    plt.close()

    '''
    All
    '''

    labels = llabels[1:18:2]
    x_pos = [np.asarray(list(dall_modes[llabels[x]].values())) for x in range(1, 18, 2)]
    y_pos = np.arange(0, 4, 0.2)
    markers = lmarkers
    colors = lcolors[1:-1:2]

    plot_energy(labels=labels, x=x_pos, y=y_pos, marker=markers,  xlabel=r'vibrational frequency (cm$^{-1}$)', ylabel='different calculations', lcolors=colors)
    
    pdf.savefig(bbox_inches='tight')
    plt.close()

    '''
    All
    '''

    labels = llabels[0:18:2]
    x_pos = [np.asarray(list(dall_modes[llabels[x]].values())) for x in range(0, 18, 2)]
    y_pos = np.arange(0, 4, 0.2)
    markers = lmarkers
    colors = lcolors[0:-1:2]

    plot_energy_windowed(labels=labels, x=x_pos, y=y_pos, marker=markers,  xlabel=r'vibrational frequency (cm$^{-1}$)', ylabel='different calculations', lcolors=colors)
    
