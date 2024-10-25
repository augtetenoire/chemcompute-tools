import numpy as np
import matplotlib.colors as colors 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages










def plot_2D(x, y, label, cmap='jet'):

    MINDEN  = 1         # uncomment to set range of colors
    MAXDEN  = 1e4   # uncomment to set range of colors
    GAMMA   = 1        # control contrast between colors: GAMMA=1 linear scaling


    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)

    bin_width, bin_length = (xmax - xmin) / 100, (ymax - ymin) / 100

    image=ax.hist2d(x=x, y=y ,cmap=cmap, label=label, bins = [np.arange(xmin,xmax, bin_width), np.arange(ymin,ymax,bin_length)],norm=colors.LogNorm(vmin=MINDEN,vmax=MAXDEN)) # use with automatic boundaries and scalings



    ax.tick_params(axis='both', which='major', length=5, width=2)
    ax.tick_params(axis='both', which='minor', length=2.5, width=1)

    # ax.xaxis.set_ticks_position('both')
    ax.tick_params(axis='both', labelsize=16)
    ax.minorticks_on()
    # ax.tick_params(axis='x', which='minor', bottom=False)

    ax.set_yscale('log')

    ax.set_xlabel('Steps (count)', fontsize=20)
    ax.set_ylabel(r'RMSE (eV/$\AA^{2}$)', fontsize=20)


