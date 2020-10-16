import numpy as np

data = np.genfromtxt(
    './FB53-Coronafallzahlen.csv',
    delimiter=';',
    names=True, # column names from first row,
    encoding='utf-8-sig', # the file has a BOM,
    dtype=None,  # guess dtypes (keeps Datum a str and the rest integer),
    missing_values='-',    # missing value indicator
)

### print(data.dtype.names)
