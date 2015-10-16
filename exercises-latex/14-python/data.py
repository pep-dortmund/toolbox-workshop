import numpy as np

# Datenfile erzeugen
np.random.seed(42)
N = 51
data_x = np.linspace(0, 2 * np.pi, N)
error_y = np.random.lognormal(-1, 0.2, size=N)
data_y = np.random.normal(np.sin(data_x), error_y)
np.savetxt(
    'data.txt',
    np.column_stack([data_x, data_y, error_y]),
    header='t/ms U/kV y_err/kV',
)
