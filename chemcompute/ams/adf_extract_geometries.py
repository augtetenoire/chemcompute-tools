#!/usr/bin/env python
# -*- coding: utf-8 -*-

import amstools
import sys
import os.path

"""
Give the file from which you want to extract file as first argument
"""

try: 
    file = sys.argv[1]
except:
    print("\nYou must give as first argument the path to the file you want to extract geometries.\n")
    sys.exit()

if os.path.isfile(file):
    print('\nExtract the geometries of:\t%s\n' % file)
    amstools.ADF_response_extract_geometries(file)