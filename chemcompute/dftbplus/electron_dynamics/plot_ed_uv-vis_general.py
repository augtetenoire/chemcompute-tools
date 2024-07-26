#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import glob

# lfiles = [str('spec-nm_d' + i + '.dat') for i in [5, 10, 15, 20, 25, 30]]
lfiles = glob.glob('spec-nm_d*.dat')
lfiles.sort()

dcolors = {
    'red': "#FF0000",
    'blue': "#0000FF",
    'green': "#00C11A",
    'turquoise': "#00FFFF",
    'black': "#000000",
    'grey': "#666666",
    'yellow': "#FFAA00",
    'pink': "#FF00EE",
    'dred': "#880000",
    'dgreen': "#008800",
    'dblue': "#000088",
    'violet': "#880088",
    'dyellow': "#888800",
    'dturquoise': "#008888",
    'orange': "#FF8800",
    'blue2': "#8800FF",
    'green2': "#88FF00",
    'pink2': "#FF0088",
    'lgreen': "#00FF88",
    'lblue': "#0088FF",
}
lcolors = [i for i in dcolors.values()] * 2



with PdfPages('UV-Vis_plot.pdf') as pdf:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Metadata informations
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    d = pdf.infodict()
    d['Title'] = ''
    d['Author'] = 'A. TETENOIRE'


    """
    PLOT all range
    """


    # Plot

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)
    for file in lfiles:
        value = np.loadtxt(file)

        ax.plot(value[:, 0], value[:, 1], label=file, linewidth=2, alpha=0.75)
        # ax.plot(value[:, 0], value[:, 1] / np.max(value[:, 1]), label=file, linewidth=2, alpha=0.75)

    # ax.set_xlim(0, 300)
    # ax.set_ylim(-0.1, 1.1)

    ax.tick_params(axis='both', which='major', length=5, width=2)
    ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    ax.tick_params(axis='both', labelsize=16)
    ax.minorticks_on()



    ax.set_xlabel('wavelength (nm)', fontsize=20)
    ax.set_ylabel('intensities (a.u.)', fontsize=20)



    ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()


    """
    PLOT in min-400 nm range
    """

    # Plot

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)
    for num, file in enumerate(lfiles):
        value = np.loadtxt(file)
        
        xmin, xmax = np.min(value), 400

        value_x_ = value[:, 0]
        value_y_ = value[:, 1]
        # filtering
        value_x = value_x_[(value_x_ < xmax) & (value_x_ > xmin)]
        value_y = value_y_[(value_x_ < xmax) & (value_x_ > xmin)]

        ax.plot(value_x, value_y, label=file, linewidth=2, alpha=0.75)
        # ax.plot(value_x, value_y / np.max(value_y), label=file, linewidth=2, alpha=0.75)


        ax.set_xlim(xmin, xmax)
        # ax.set_ylim(-0.1, 1.1)


        ax.tick_params(axis='both', which='major', length=5, width=2)
        ax.tick_params(axis='both', which='minor', length=2.5, width=1)

        ax.tick_params(axis='both', labelsize=16)
        ax.minorticks_on()


        ax.set_xlabel('wavelength (nm)', fontsize=20)
        ax.set_ylabel('intensities (a.u.)', fontsize=20)


        ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()






    """
    PLOT in 400-800 nm range
    """

    # Plot

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)
    for num, file in enumerate(lfiles):
        value = np.loadtxt(file)
        
        xmin, xmax = 400, 800

        value_x_ = value[:, 0]
        value_y_ = value[:, 1]
        # filtering
        value_x = value_x_[(value_x_ < xmax) & (value_x_ > xmin)]
        value_y = value_y_[(value_x_ < xmax) & (value_x_ > xmin)]

        ax.plot(value_x, value_y, label=file, linewidth=2, alpha=0.75)
        # ax.plot(value_x, value_y / np.max(value_y), label=file, linewidth=2, alpha=0.75)


        ax.set_xlim(xmin, xmax)
        # ax.set_ylim(-0.1, 1.1)


        ax.tick_params(axis='both', which='major', length=5, width=2)
        ax.tick_params(axis='both', which='minor', length=2.5, width=1)

        ax.tick_params(axis='both', labelsize=16)
        ax.minorticks_on()


        ax.set_xlabel('wavelength (nm)', fontsize=20)
        ax.set_ylabel('intensities (a.u.)', fontsize=20)


        ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()


    """
    PLOT in 750-max nm range
    """

    # Plot

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)
    for num, file in enumerate(lfiles):
        value = np.loadtxt(file)
        
        xmin, xmax = 750, np.max(value)

        value_x_ = value[:, 0]
        value_y_ = value[:, 1]
        # filtering
        value_x = value_x_[(value_x_ < xmax) & (value_x_ > xmin)]
        value_y = value_y_[(value_x_ < xmax) & (value_x_ > xmin)]

        ax.plot(value_x, value_y, label=file, linewidth=2, alpha=0.75)
        # ax.plot(value_x, value_y / np.max(value_y), label=file, linewidth=2, alpha=0.75)


        ax.set_xlim(xmin, xmax)
        # ax.set_ylim(-0.1, 1.1)


        ax.tick_params(axis='both', which='major', length=5, width=2)
        ax.tick_params(axis='both', which='minor', length=2.5, width=1)

        ax.tick_params(axis='both', labelsize=16)
        ax.minorticks_on()


        ax.set_xlabel('wavelength (nm)', fontsize=20)
        ax.set_ylabel('intensities (a.u.)', fontsize=20)


        ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=4)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()
