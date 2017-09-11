import numpy as np

# Aufgabe 1)

a = np.array([2, 3, 5, 7, 11, 13, 17, 19])
b = np.arange(0, 10)
c = np.arange(0, 20, 2)
d = np.linspace(0, 5, num=11)

print("Aufgabe 1)")
print("Array a)", a)
print("Array b)", b)
print("Array c)", c)
print("Array d)", d)

# Aufgabe 2)
print("Aufgabe 2)")
print("Array a)")
print("\t len(a)", len(a))
print("\t a.shape", a.shape)
print("Array b)")
print("\t len(b)", len(b))
print("\t b.shape", b.shape)
print("Array c)")
print("\t len(c)", len(c))
print("\t c.shape", c.shape)
print("Array d)")
print("\t len(d)", len(d))
print("\t d.shape", d.shape)

# Aufgabe 3)
# Nur Array b) und c) lassen sich addieren, bei allen anderen passen die Größen nicht zusammen.
print("Aufgabe 3)")
print("Array b + c", b + c)


# Aufgabe 4)
print("Aufgabe 4)")
# Anzahl der Zeilen ist die Anzahl der Elemente in b (ein Element pro Zeile), Anzahl der Spalten ist damit 1
# Das Produkt aus den Argumenten von reshape muss immer der Anzahl an Elementen entsprechen.
c_2d = b.reshape(len(c), 1)
print("Array c_2d (mit len(b))", c_2d)
# Man kann eine Dimension mit einer -1 versehen, diese wird dann automatisch ausgerechnet.
c_2d = b.reshape(-1, 1)
print("Array c_2d (mit -1)", c_2d)


# Aufgabe 5)
print("Aufgabe 5)")
print("Array b)", b)
print("Array c_2d", c_2d)
print("Array b + c_2d", b + c_2d)
