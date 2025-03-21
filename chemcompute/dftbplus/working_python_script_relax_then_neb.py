from ase.io import read, write
from ase.neb import NEB
from ase.optimize import BFGS
from ase.calculators.dftb import Dftb
from ase.constraints import FixAtoms


# Load states already converged with DFTB+
initial = read('geom.initial.gen')
final = read('geom.final.gen')
"""
# Freez Au slab
constraint = FixAtoms(mask=[atom.symbol == 'Au' for atom in initial])
# constraint = FixAtoms(indices=[x for x in range(0, 169)])
initial.set_constraint(constraint)
final.set_constraint(constraint)
"""
# Converge initial state
calcs = Dftb(label='output_CO_initial')
initial.set_calculator(calcs)
opt_initial = BFGS(initial, trajectory='initial.traj')
opt_initial.run(fmax=1.00E-02)

# Converge final state
calcs = Dftb(label='output_CO_final')
final.set_calculator(calcs)
opt_final = BFGS(final, trajectory='final.traj')
opt_final.run(fmax=1.00E-02)






#============================
#           NEB
#============================


NIMAGES = 5

def main():
    '''Main driver routine.'''

    initial = read('initial.traj')
    final = read('final.traj')


    images = [initial]
    images += [initial.copy() for ii in range(NIMAGES)]
    images += [final]
    
    # constraint = FixAtoms(mask=[atom.symbol == 'Au' for atom in initial])
    constraint = FixAtoms(indices=[x for x in range(0, 1017)])
    for image in images:
        image.set_constraint(constraint)
    


    calcs = [Dftb(label='CO-2cluster',
                # kpts=(1, 1, 1),
                # Hamiltonian_SCC='Yes',
                # Hamiltonian_SCCTolerance='1.00E-06',
                # Hamiltonian_MaxAngularMomentum_Au='"d"',
                # Hamiltonian_MaxAngularMomentum_O='"p"',
    )
             for ii in range(NIMAGES)]

    for ii, calc in enumerate(calcs):
        images[ii + 1].set_calculator(calc)

    # neb = NEB(images, climb=True, parallel=True, method='improvedtangent')#doesn't work
    # neb = NEB(images) # works
    # neb = NEB(images, climb=True, method='improvedtangent') #doesn't work
    neb = NEB(images, climb=True) #works
    neb.interpolate(apply_constraint=False)
    # neb.interpolate()
    write('XDATCAR_interpolate', images, format='vasp-xdatcar')
    write('images_interpolate.xyz', images, format='xyz')

    opt = BFGS(neb, trajectory='i2f.traj') 


    opt.run(fmax=5.00E-02)


if __name__ == "__main__":
    main()



# ase gui i2f.traj@-5:
# ase nebplot --share-x --share-y i2f.traj
