#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



data = np.loadtxt('molpopul1.dat', skiprows=2)



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


with PdfPages('orbital_population_plot.pdf') as pdf:
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Metadata informations
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    d = pdf.infodict()
    d['Title'] = ''
    d['Author'] = 'A. TETENOIRE'


    """
    PLOT
    """


    # Plot

    fig=plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(111)
    for num in range(1, len(data[0])):
        

        ax.plot(data[:, 0], data[:, num], label=str('orbital-%i' % num), linewidth=2, alpha=0.75)

        # Parameters
        # ax.xaxis.set_ticks([1, 2, 3, 4])
        # ax.set_ylim(-6, -1)
        # ax.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
        # ax.yaxis.set_ticks(np.arange(-6, 0, 1))

        # ax.set_xlim(xmin, xmax)
        # ax.set_ylim(-0.1, 1.1)

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

        ax.set_xlabel('time (fs)', fontsize=20)
        ax.set_ylabel('Orbital population', fontsize=20)

        # ax.legend(fontsize=10, ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.15), frameon=False,  labelspacing=0.2, handletextpad=0.2, columnspacing=1)   
        # ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(0.9, 1), frameon=False)


        ax.legend(fontsize=10, loc='lower center', bbox_to_anchor=(0.5, 1), frameon=False, ncols=6)

    


    pdf.savefig(bbox_inches='tight')
    plt.close()
