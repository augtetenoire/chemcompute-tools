#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
"""

import numpy as np
import os.path 





def ADF_response_load_modes_out(file):
    with open(file, 'r') as foo:
        llines = foo.readlines()
    load = False
    dmodes = {}
    for line in llines:
        if 'Normal Modes' in line:
            load = True
        if (load) and ('Mode:' in line):
            mode_nb, freq, intensity = int(line.split()[1]), float(line.split()[4]), float(line.split()[7])
            dmodes[mode_nb] = np.asarray([freq, intensity])
        if 'Statistical' in line:
            load = False
    return dmodes


def ADF_response_extract_vibration_modes(file, write_jmol_file=True, nb_image=20):
 
    path = os.path.dirname(file)
    if path == '':
        path = '.'

    with open(file, 'r') as foo:
        llines = foo.readlines()

    load_1 = False
    load_2 = False
    load_geom_1 = False
    load_geom_2 = False
    geometry_already_loaded = False

    dmodes = {}
    lgeometry = []
    lmoves = []
    for line in llines:

        # load Geometry
        if load_geom_1 and load_geom_2  and ('FRAGMENTS' not in line) and (not geometry_already_loaded):
            lgeometry.append(line.split()[1:5])
        if 'G E O M E T R Y' in line:
            load_geom_1 = True
        if ('--------------------------' in line) and load_geom_1:
            load_geom_2 = True
        if ('FRAGMENTS' in line):
            load_geom_1 = False
            load_geom_2 = False
            if lgeometry:
                lgeometry.pop(-1)
                geometry_already_loaded = True

        if 'PES point character' in line:
            load_1 = False
            load_2 = False
            if lmoves:
                dmodes[mode] = {}
                dmodes[mode]['frequency'] = frequency
                dmodes[mode]['intensity'] = intensity
                lmoves.pop(-1)
                dmodes[mode]['moves'] = np.asarray(lmoves)
                lmoves = []

        # load modes
        if load_1 and load_2 and ('Mode:' not in line) and ('Index' not in line) and ('Displacements' not in line) and ('removed' not in line):
            lmoves.append(line.split()[2:])

        if 'Normal Modes' in line:
            load_1 = True

        if load_1 and ('Mode:' in line) and ('Frequency' in line):
            load_2 = True
            if lmoves:
                dmodes[mode] = {}
                dmodes[mode]['frequency'] = frequency
                dmodes[mode]['intensity'] = intensity
                lmoves.pop(-1)
                dmodes[mode]['moves'] = np.asarray(lmoves)
                lmoves = []

            mode, frequency, intensity = int(line.split()[1]), float(line.split()[4]), float(line.split()[7])


    # Write configuration files
    filename = str(path + '/configuration.xyz')
    with open(filename, 'w+') as foo:
        foo.write(str(str(len(lgeometry)) + '\n'))
        foo.write(str('Geometry\n'))
        for coordinate in lgeometry:
            foo.write('\t'.join(coordinate))
            foo.write('\n')

    # write files jmol files
    if write_jmol_file:
        for key in dmodes.keys():
            # print('\nWrite mode %s' % str(key))
            filename = str(path + '/jmol_mode_%03d.xyz' % key)
            with open(filename, 'w+') as foo:
                foo.write(str(str(len(dmodes[key]['moves'])) + '\n'))
                foo.write(str('Vibrational mode: %s\t frequency=%s cm-1\tintensity=%s kJ/mol\n' % (str(key), dmodes[key]['frequency'], dmodes[key]['intensity'])))
                for num, move in enumerate(dmodes[key]['moves']):
                    foo.write('\t'.join(lgeometry[num]))
                    foo.write('\t')
                    foo.write('\t'.join(move))
                    foo.write('\n')
    
    # Write mode file like a video, not using the forces
    position_as_number = np.asarray(lgeometry)[:, 1:].astype(float)
    for key in dmodes.keys():
        # print('\nWrite mode %s' % str(key))
        filename = str(path + '/mode_%03d.xyz' % key)
        with open(filename, 'w+') as foo:

            move_as_number = dmodes[key]['moves'].astype(float)
            # start from negative and finish to positive forces and go backward
            step = 0
            for image_count in range(-int(nb_image / 2), int(nb_image / 2), 1):
                
                step += 1 
                foo.write(str(str(len(dmodes[key]['moves'])) + '\n'))
                foo.write(str('Step %i -- > Vibrational mode: %s\t frequency=%s cm-1\tintensity=%s kJ/mol\n' % (step, str(key), dmodes[key]['frequency'], dmodes[key]['intensity'])))
                new_position = position_as_number + image_count * (move_as_number / (nb_image / 2))
                
                for nb_atom in range(len(new_position)):
                    
                    foo.write(lgeometry[nb_atom][0])
                    foo.write('\t')
                    foo.write('\t'.join(new_position[nb_atom].astype(str)))
                    foo.write('\n')
            # Go backward
            for image_count in range(int(nb_image / 2), -int(nb_image / 2), -1):
                
                step += 1 
                foo.write(str(str(len(dmodes[key]['moves'])) + '\n'))
                foo.write(str('Step %i -- > Vibrational mode: %s\t frequency=%s cm-1\tintensity=%s kJ/mol\n' % (step, str(key), dmodes[key]['frequency'], dmodes[key]['intensity'])))
                new_position = position_as_number + image_count * (move_as_number / (nb_image / 2))
                
                for nb_atom in range(len(new_position)):
                    
                    foo.write(lgeometry[nb_atom][0])
                    foo.write('\t')
                    foo.write('\t'.join(new_position[nb_atom].astype(str)))
                    foo.write('\n')





def AMS_Raman_load_modes_out(file):
    with open(file, 'r') as foo:
        llines = foo.readlines()
    load_1 = False
    load_2 = False
    dmodes = {}
    for line in llines:
        if 'Raman Intensities' in line:
            load_1 = True
        if (load_1) and ('Index' in line):
            load_2 = True
        if ('------------' in line) and (load_2):
            load_1 = False
        if (load_1) and (load_2) and (line != '\n') and ('Index' not in line):
            mode_nb, freq, intensity = int(line.split()[0]), float(line.split()[1]), float(line.split()[2])
            dmodes[mode_nb] = np.asarray([freq, intensity])
    return dmodes


def AMS_normal_modes_load_modes_out(file):
    with open(file, 'r') as foo:
        llines = foo.readlines()
    load_1 = False
    load_2 = False
    dmodes = {}
    for line in llines:
        if 'Normal Mode Frequencies' in line:
            load_1 = True
        if (load_1) and ('Index' in line):
            load_2 = True
        if 'Zero-point energy' in line:
            load_1 = False
        if (load_1) and (load_2) and (line != '\n') and ('Index' not in line):
            mode_nb, freq, intensity = int(line.split()[0]), float(line.split()[1]), float(line.split()[2])
            dmodes[mode_nb] = np.asarray([freq, intensity])
    return dmodes



def ADF_response_extract_geometries(file):

    path = os.path.dirname(file)
    if path == '':
        path = '.'

    with open(file, 'r') as foo:
        llines = foo.readlines()

    load = False
    load_geom_1 = False
    lgeometry = []
    lconfigurations = []
    for line in llines:

        if '*  GEOMETRY OPTIMIZATION  *' in line:
            load = True

        # load Geometry
        if load :
            if load_geom_1   and ('Total System Charge' not in line):
                lgeometry.append(line.split()[1:])
            if ('x (angstrom)   y (angstrom)   z (angstrom)' in line):
                load_geom_1 = True
            if ('Total System Charge' in line):
                load_geom_1 = False
                if lgeometry:
                    lgeometry.pop(-1)
                    lconfigurations.append(lgeometry)
                    lgeometry = []

        if '** CONVERGED **' in line:
            load = False

    # If there is configuration to write
    if lconfigurations:

        # Write configuration files
        filename = str(path + '/configurations.xyz')
        with open(filename, 'w+') as foo:
            for num in range(len(lconfigurations)):
                foo.write(str(str(len(lconfigurations[0])) + '\n'))
                foo.write(str('Optimization step %i\n' % num))
                for coordinate in lconfigurations[num]:
                    foo.write('\t'.join(coordinate))
                    foo.write('\n')


        # Write configuration files
        filename = str(path + '/first_configuration.xyz')
        with open(filename, 'w+') as foo:
            foo.write(str(str(len(lconfigurations[0])) + '\n'))
            foo.write(str('Optimization step 0\n'))
            for coordinate in lconfigurations[0]:
                foo.write('\t'.join(coordinate))
                foo.write('\n')

        # Write configuration files
        filename = str(path + '/last_configuration.xyz')
        with open(filename, 'w+') as foo:
            foo.write(str(str(len(lconfigurations[0])) + '\n'))
            foo.write(str('Optimization step %i\n' % (len(lconfigurations) - 1)))
            for coordinate in lconfigurations[-1]:
                foo.write('\t'.join(coordinate))
                foo.write('\n')


def AMS_scanning_load_modes_out(file):
    with open(file, 'r') as foo:
        llines = foo.readlines()
    load_1 = False
    load_2 = False
    count = 0
    dmodes = {}
    for line in llines:
        if 'Mode Scanning Results' in line:
            load_1 = True
        if (load_1) and ('Frequency (New)' in line):
            load_2 = True
        if 'Mode Scanning finished' in line:
            load_1 = False
        if (load_1) and (load_2) and ('Mode' in line):
            count += 1
            freq, intensity = float(line.split()[2]), float(line.split()[3])
            dmodes[count] = np.asarray([freq, intensity])
    return dmodes

