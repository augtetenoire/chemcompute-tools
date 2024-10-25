import numpy as np
import shlex
import re



class configuration:
    """Docstring"""

    def __init__(self, properties=None, latoms=None, energy=None, lpos=None, lforces=None, pbc=None, lattice=None, config_type=None, dihedral_angle=None):
        """
        properties: string that contain the properties written in the extendend xyz file (ex: 'species:S:1:pos:R:3:forces:R:3')
        latoms: (string) list of atoms species as string in xyz of length n
        energy: energy of the configuration
        lpos: list of position (n, 3) for n atoms
        lforces: list of forces (n, 3) for n atoms
        lattice: list of the component of the lattice vectors of size 9
        pbc: periodic boudary conditions as : F F F for False False False
        config_type: 'isolated_atom' or a specific note
        dihedral_angle: _JSON[a,b,c] or scalar
        """
        self.properties = properties
        self.latoms = latoms
        self.pbc = pbc
        self.config_type = config_type

        # Scalar type
        if type(latoms) != type(None):
            self.natoms = len(latoms)
        else:
            self.natoms = None
        if type(energy) != type(None):
            self.energy = float(energy)
        else:
            self.energy = None
        if type(dihedral_angle) != type(None):
            self.dihedral_angle = float(dihedral_angle)
        else:
            self.dihedral_angle = None

        # List type (directly transform to np.array)
        if type(lpos) != type(None):
            self.lpos = np.asarray([np.asarray([float(y) for y in x]) for x in lpos])
        else:
            self.lpos = None
        if type(lforces) != type(None):
            self.lforces = np.asarray([np.asarray([float(y) for y in x]) for x in lforces])
        else:
            self.lforces = None
        if type(lattice) != type(None):
            self.lattice = np.asarray([float(x) for x in lattice])
        else:
            self.lattice = None
        


    
    def read_header(self, tupple_header):
        for i in range(len(tupple_header)):
            if "Lattice" in b[i]:
                self.lattice = re.findall(r"[-+]?(?:\d*\.*\d+)", b[i])
            elif "Properties" in b[i]:
                self.properties = b[i].replace('Properties=', '')
            elif "dihedral_angle" in b[i]:
                self.dihedral_angle = float(re.findall(r"[-+]?(?:\d*\.*\d+)", b[i])[0])
            elif "energy" in b[i]:
                self.energy = float(b[i].replace('energy=', ''))
            elif "pbc" in b[i]:
                self.pbc = " ".join(re.split("[^FT]*", b[i]))
            elif "config_type" in b[i]:
                 self.config_type = b[i].replace('config_type=', '')

    
    def read_conf(self, extracted_tupple):
        """
        """
        self.natoms = int(extracted_tupple[0])
        self.read_header(extracted_tupple[1])

        if "species:S:" in self.properties:
            self.latoms = []
        if "pos:R:3" in self.properties:
            self.lpos = []
        if "forces:R:3" in self.properties:
            self.lforces = []
        
        for i in range(self.natoms):
            string = extracted_tupple[2][i].split()
            if "species:S:" in self.properties:
                self.latoms.append(string[0])
            if "pos:R:3" in self.properties:
                self.lpos.append([float(x) for x in string[1:4]])
            if "forces:R:3" in self.properties:
                self.lforces.append([float(x) for x in string[4:7]])
        self.lpos = np.asarray(self.lpos)
        self.lforces = np.asarray(self.lforces)

    
    def write_conf(self, filename, mode='w'):
        """
        mode: can be write 'w' or append 'a'
        """

        if mode == "w":
            with open(filename, mode=mode) as foo:
                
                foo.write(str(self.natoms))
                foo.write("\n")
                
                # Write Header
                if type(self.lattice) != type(None):
                    lattice = [str(x) for x in self.lattice]
                    foo.write(str( " Lattice=\""+ ' '.join(lattice) + "\""))
                foo.write(str(" Properties=" + ''.join(self.properties)))
                if self.dihedral_angle:
                    foo.write(str(" dihedral_angle=%s" % self.dihedral_angle))
                foo.write(str(" config_type=%s" % self.config_type))
                foo.write(str(" energy=%s" % self.energy))
                if self.pbc:
                    foo.write(str(" pbc=\"" + " ".join(self.pbc) + "\""))
                
                # Write xyz
                for i in range(len(self.latoms)):
                    foo.write("\n")
                    foo.write(str(self.latoms[i] + '{:15.8f}'.format(self.lpos[i][0]) + '{:15.8f}'.format(self.lpos[i][1]) + '{:15.8f}'.format(self.lpos[i][2])))
                    if type(self.lforces) != type(None):
                        foo.write(str('{:15.8f}'.format(self.lforces[i][0]) + '{:15.8f}'.format(self.lforces[i][1]) + '{:15.8f}'.format(self.lforces[i][2])))

                              
        elif mode == "a":
            with open(filename, mode=mode) as foo:
                
                foo.write(str(self.natoms))
                foo.write("\n")
                
                # Write Header
                if type(self.lattice) != type(None):
                    lattice = [str(x) for x in self.lattice]
                    foo.write(str( " Lattice=\""+ ' '.join(lattice) + "\""))
                foo.write(str(" Properties=" + ''.join(self.properties)))
                if self.dihedral_angle:
                    foo.write(str(" dihedral_angle=%s" % self.dihedral_angle))
                foo.write(str(" config_type=%s" % self.config_type))
                foo.write(str(" energy=%s" % self.energy))
                if self.pbc:
                    foo.write(str(" pbc=\"" + " ".join(self.pbc) + "\""))
                
                # Write xyz
                for i in range(len(self.latoms)):
                    foo.write("\n")
                    foo.write(str(self.latoms[i] + '{:15.8f}'.format(self.lpos[i][0]) + '{:15.8f}'.format(self.lpos[i][1]) + '{:15.8f}'.format(self.lpos[i][2])))
                    if type(self.lforces) != type(None):
                        foo.write(str('{:15.8f}'.format(self.lforces[i][0]) + '{:15.8f}'.format(self.lforces[i][1]) + '{:15.8f}'.format(self.lforces[i][2])))

                foo.write("\n")

                              



def extract_data(conf_data):
    """
    Input the 'string_data' variable of the 'read_extended_file' function. It outputs the content of the extended file such as tupple containing 3 element, time the number of configuration. 
    tupple[x][0]: the number of atom in the configuration
    tupple[x][1]: the header of the configuration
    tupple[x][2]: the xyz file of the configuration (element, position, forces)

    """
    index_properties = [i for i, value in enumerate(conf_data) if ("Properties" in value)]
    ltupple = []
    for i in index_properties:
        number = int(conf_data[i-1])
        # print(i+1, i + number+1)
        xyz = conf_data[i+1:i + number+1]
        properties = shlex.split(conf_data[i])
        ltupple.append((number, properties, xyz))
    return ltupple



def read_extended_file(filepath):
    """
    Input an extended file to get directly the 'configuration' object defined by the class above. It reads all the configurations of the file.
    """
    # Load data in string
    with open(filepath) as foo:
        string_data = foo.readlines()
    string_data = [x.replace('\n', '') for x in string_data]

    # extract all conf in tupples
    extracted_data = extract_data(string_data)
    # put tupples into configuration object
    lconfs = []
    for i in range(len(extracted_data)):
        conf = configuration()
        conf.read_conf(extracted_data[i])
        lconfs.append(conf)
        
    return lconfs