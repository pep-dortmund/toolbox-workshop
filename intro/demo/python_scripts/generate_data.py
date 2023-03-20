import numpy as np

rng = np.random.default_rng(43)
N = 30
x_new = rng.normal(0.0, 0.3, N)
data_x = np.linspace(0, 2, N)
error_y = rng.lognormal(-1, 0.02, size=N)
data_y = rng.normal(4 * data_x, error_y)
np.savetxt(
    "daten.txt",
    np.column_stack([data_x, data_y]),
    header="x/min\ty/m",
    fmt="%.3f %.3f"
)
