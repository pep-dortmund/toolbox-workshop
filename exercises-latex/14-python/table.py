import itertools

import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (
    nominal_values as noms,
    std_devs as stds,
)

def make_table(columns, figures=None):
    if figures is None:
        figures = [None] * len(columns)

    cols = []
    for column, figure in zip(columns, figures):
        if np.any(stds(column)):
            if figure is None:
                figure = ''
            col = list(zip(*['{0:.{1:}uf}'.format(x, figure).split('+/-') for x in column]))
        else:
            col = list(zip(*[['{0:.{1:}f}'.format(x, figure)] for x in noms(column)]))
        cols.extend(col)

    max_lens = [max(len(s) for s in col) for col in cols]
    cols = [['{0:<{1:}}'.format(s, ml) for s in col] for col, ml in zip(cols, max_lens)]

    rows = list(itertools.zip_longest(*cols))

    return (r' \\' + '\n').join([' & '.join(s for s in row if s is not None) for row in rows]) + r' \\'

def make_SI(num, unit, exp='', figures=None):
    if np.any(stds([num])):
        if figures is None:
            figures = ''
        x = '{0:.{1:}uf}'.format(num, figures).replace('/', '')
    else:
        x = '{0:.{1:}f}'.format(num, figures)

    return r'\SI{{{}{}}}{{{}}}'.format(x, exp, unit)

def write(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
        if not content.endswith('\n'):
            f.write('\n')
