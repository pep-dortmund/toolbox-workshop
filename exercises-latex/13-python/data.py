import numpy as np

# Datenfile erzeugen
rng = np.random.default_rng(42)
N = 51
data_x = np.linspace(0, 2 * np.pi, N)
error_y = rng.lognormal(-1, 0.2, size=N)
data_y = rng.normal(2 * np.sin(1.5 * data_x + np.pi / 4) + 0.5, error_y)
np.savetxt(
    "data.txt",
    np.column_stack([data_x, data_y, error_y]),
    header="t/ms U/kV y_err/kV",
)
