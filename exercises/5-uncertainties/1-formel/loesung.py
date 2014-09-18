
from uncertainties import ufloat
from uncertainties.unumpy import sin

x = ufloat(4.56, 0.2)
y = ufloat(2.11, 0.3)
z = ufloat(10, 1)

Q = x**2 * sin(y) + z

print('Q = {}'.format(Q))

from sympy import var, sin

x, y, z = var('x y z')

Q = x**2 * sin(y) + z

print(Q.diff(x))
print(Q.diff(y))
print(Q.diff(z))


