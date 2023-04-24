import numpy as np
from ase.io import read
from ase.build import make_supercell
from ase.geometry.analysis import Analysis

def analysis_bond_inner(atoms, type_map):
    '''
    type_map=['Li','La','H']
    return: min dis of different type bonds including
             `Li-La`, `Li-H`, `La-H`, `Li-Li`, `La-La`, `H-H`
    '''
    diff_bond_type = list(map(list, combinations(type_map, 2)))
    for same_type in type_map:
        diff_bond_type.extend([[same_type,same_type]])

    bond_situation = {}
    for each_type in diff_bond_type:
        bond_situation_key = ''.join(each_type)
        ana = Analysis(atoms)
        bond_indice = ana.get_bonds(each_type[0], each_type[1], unique=True)
        if bond_indice == [[]]:
            min_dis = np.array(203)
            #min_dis = np.nan
        else:
            bond_value = ana.get_values(bond_indice)
            min_dis = np.nanmin(bond_value[0])
        bond_situation[bond_situation_key] = min_dis

    return bond_situation

def calc_min_dis(ase_stru):
    '''
    calculate min dis of given strucutre
    '''
    dis_mtx = ase_stru.get_all_distances(mic=True)
    row,col = np.diag_indices_from(dis_mtx)
    #dis_mtx[row,col] = 1000
    dis_mtx[row,col] = np.nan
    min_dis = np.nanmin(dis_mtx)

    return min_dis

def volume_per_atom(atoms):
    volume = atoms.get_volume()
    natoms = atoms.get_global_number_of_atoms()
    return (volume / natoms)

def density(atoms):
    volume = atoms.get_volume()
    mass = atoms.get_masses().sum()
    return (mass / volume)

def calc_rdf(atoms, rmax=5, nbins=50):

    min_cell_par = min(atoms.cell.cellpar()[:3])
    P = np.eye(3) * (10 // min_cell_par + 1)
    new_atoms = make_supercell(atoms, P)

    return Analysis(atoms).get_rdf(rmax=rmax, nbins=nbins, )
    

atoms = read('CONTCAR')
key_situation = analysis_bond_inner(atoms, ['La', 'H'])
print(key_situation)
print(np.array(list(key_situation.values()))*0.85)
print(calc_min_dis(atoms))
