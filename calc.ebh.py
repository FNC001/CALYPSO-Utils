from pymatgen.analysis.phase_diagram import PDEntry, PhaseDiagram, PDPlotter, CompoundPhaseDiagram, TransformedPDEntry
from pymatgen.core.composition import Composition
from pymatgen.core.periodic_table import DummySpecies, Element
import plotly.express as px
import pandas as pd
import numpy as np

ini_entries = []
convexhull_data = pd.read_csv('./convexhull.dat', header=0, sep=r'\s+')

for idx, row in convexhull_data.iterrows():
    #if row['form_energy'] <= 0.02:
    comp = Composition(row['FORMULA'])
    num_atoms = comp.num_atoms
    enth_per_atom = row['ENTH']
    enth = enth_per_atom * num_atoms
    entry_id = row['NAMEs']
    _entry = PDEntry(comp, enth)
    _entry.entry_id = entry_id
    # _entry.spg = row['spg']
    # _entry.p = row['P']
    # _entry.nsw = row['NSW']
    # _entry.epa = enth_per_atom
    ini_entries.append(_entry)              
ini_pd = PhaseDiagram(ini_entries)
plotter = PDPlotter(ini_pd, show_unstable=0.050, backend='plotly')
plotter.get_plot().write_image('convexhull.png')     


e_above_hull = []
form_energy = []
names = []
nsws = []
formulas = []
enths = []
spgs = []
ps = []
threshold_start = 0.00
#threshold = 0.05

for entry in ini_entries:
    ebh = ini_pd.get_e_above_hull(entry, )
    fme = ini_pd.get_form_energy_per_atom(entry)
    name = entry.entry_id
    # spg = entry.spg
    # p = entry.p
    formula = entry.composition.formula.replace(".", "")
    #if threshold_start <= ebh <= threshold:
    e_above_hull.append(ebh)
    form_energy.append(fme)
    names.append(name)
    formulas.append(''.join(  (''.join(str(formula))).split()  ))
    # spgs.append(spg)
    # ps.append(p)
    # enths.append(enth)


df = pd.DataFrame(
    {
        'formula':formulas,
        'e_above_hull':e_above_hull,
        # 'spg':spgs,
        # 'p':ps,
        'form_energy':form_energy,
        'name':names,
        }
    )
df.to_csv('./e_above_hull_50meV.csv', index=False, sep=' ')
