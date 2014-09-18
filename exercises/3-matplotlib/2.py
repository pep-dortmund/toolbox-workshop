# encoding: utf-8

from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
for A in (-1, -.5, .5, 1):
    plt.plot(x, A * np.cos(x), label='$A = {}$'.format(A))
plt.legend()
plt.xlim([0, 2 * np.pi])
plt.savefig('Acosx.pdf')
