# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

from pylab import *

x = linspace(0, 1)

plot(x, x**2, 'b-', label=r'$x^2$')
plot(x, x**5, 'gx', label=r'$x^5$')
xlabel(r'$x$')
legend(loc='best')
savefig('2.pdf')
