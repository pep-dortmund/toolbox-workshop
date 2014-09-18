# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

from pylab import *

x = linspace(0, 2 * pi)

plot(x, sin(x), 'r-', label=r'$\sin(x)$')
plot(x, cos(x), 'b--', label=r'$\cos(x)$')
xlim(0, 2 * pi)
ylim(-1.2, 1.2)
xlabel(r'$x$')
xticks([0, pi / 2, pi, 3 * pi / 2, 2 * pi], ['$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
legend(loc='best')
tight_layout()
savefig('5.pdf', bbox_inches='tight', pad_inches=0)
