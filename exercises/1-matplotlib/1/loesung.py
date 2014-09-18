# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

from pylab import *

x = linspace(0, 1)

plot(x, x**2, 'b-')
xlabel(r'$x$')
ylabel(r'$x^2$')
savefig('1.pdf')
