# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

from pylab import *

# Datenfile erzeugen
data_x = linspace(0, 2 * pi, 50)
data_y = sin(data_x)
data_x += 0.1 * randn(50)
data_y += 0.2 * randn(50)
error_x = 0.1 * 0.5 * randn(50)
error_y = 0.2 * 0.5 * randn(50)
savetxt('4.txt', array([data_x, error_x, data_y, error_y]).T)

x, e_x, y, e_y = loadtxt('4.txt', unpack=True)
errorbar(x, y, xerr=e_x, yerr=e_y, fmt='rx', label='Daten')
t = linspace(-0.5, 2 * pi + 0.5)
plot(t, sin(t), 'b-', label='"Fit"')
xlim(t[0], t[-1])
xlabel(r'$t$')
ylabel(r'$f(t)$')
legend(loc='best')
savefig('4.pdf')
