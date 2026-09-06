# begin solution
from sympy import sin, var
from uncertainties import ufloat
from uncertainties.unumpy import sin as usin

x = ufloat(4.56, 0.2)
y = ufloat(2.11, 0.3)
z = ufloat(10, 1)

Q = x**2 * usin(y) + z

print(f"Q = {Q}")
print(Q.n, Q.s)

x, y, z = var("x y z")

Q = x**2 * sin(y) + z

print(f"d/dx {Q} = {Q.diff(x)}")
print(f"d/dy {Q} = {Q.diff(y)}")
print(f"d/dz {Q} = {Q.diff(z)}")
# end solution
