# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

from pylab import *

# Datenfile erzeugen
data_x = linspace(0, 10, 100)
data_y = 10 * exp(-data_x)
savetxt('3.txt', array([data_x, data_y]).T)

x, y = loadtxt('3.txt', unpack=True)
subplot(1, 2, 1)
plot(x, y, 'rx')
xlabel(r'$x$')
ylabel(r'$y$')
subplot(1, 2, 2)
plot(x, y, 'rx')
xlabel(r'$x$')
ylabel(r'$y$')
yscale('log')
tight_layout()
savefig('3.pdf')
