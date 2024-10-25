#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ase.io
from sys import argv, exit
from os.path import basename
import argparse


# parser = argparse.ArgumentParser(
#                     prog='ase_converter',
#                     description=
# """
# Convert the input file in output format
# used format

# gaussian-in
# gaussian-out
# gen
# dftb
# cif
# vasp
# vasp-xdatcar
# xyz

# """,
#                     epilog='Text at the bottom of help')


if len(argv) <= 1:
    exit('Precise the file in argument')
elif len(argv) == 4:
    file = argv[1]
    output = str(argv[2])
    output_name = str(argv[3])
else:
    print('Give as input:\t file output_format  output_name')


# parser.add_argument('string', metavar='file', type=str, nargs='+',
#                     help='file that should be converted')

print('\nLoad\t%s' % file)
a = ase.io.read(file)


# basefile = basename(file)
# filename = file.replace(basefile, output_name)
filename = output_name
print('\nWrite\t%s' % filename)
ase.io.write(filename, a, format=output)