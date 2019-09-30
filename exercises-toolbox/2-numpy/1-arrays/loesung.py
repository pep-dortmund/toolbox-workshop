import numpy as np

# Aufgabe 1)

a = np.zeros(shape=3)
b = np.ones(shape=4)
c = 2*np.ones(shape=5)
d = np.array([2, 3, 5, 7, 11, 13, 17, 19])
e = np.arange(0, 10)
f = np.arange(0, 20, 2)
g0 = np.linspace(0, 5, num=11)
g1 = np.arange(0, 5.5, step=0.5)
h = 3*np.ones(shape=(3, 3))


array_names = ["a", "b", "c", "d", "e", "f", "g0", "g1", "h"]
arrays = [a, b, c, d, e, f, g0, g1, h]

print("Aufgabe 1)")
for name, array in zip(array_names, arrays):
    print(f"Array {name}: {array}")


# Aufgabe 2)
print("\nAufgabe 2)")
for name, array in zip(array_names, arrays):
    print(f"Array {name}")
    print(f"\t len({name}): {len(array)}")
    print(f"\t {name}.shape: {array.shape}")

# Aufgabe 3)
# Nur Array e) und f) lassen sich addieren, bei allen anderen passen die Größen nicht zusammen.
print("\nAufgabe 3)")
print(f"Array d + f: {e + f}")


# Aufgabe 4)
print("\nAufgabe 4)")
# Anzahl der Zeilen ist die Anzahl der Elemente in f (ein Element pro Zeile), Anzahl der Spalten ist damit 1
# Das Produkt aus den Argumenten von reshape muss immer der Anzahl an Elementen entsprechen.
e_2d = e.reshape(1, len(e))
print(f"Array e.reshape(1, len(e)):\n{e_2d}")
# Man kann eine Dimension mit einer -1 versehen, diese wird dann automatisch ausgerechnet.
e_2d = e.reshape(1, -1)
print(f"Array e.reshape(1, -1):\n{e_2d}")

f_2d = f.reshape(len(f), 1)
print(f"Array f.reshape(len(f), 1):\n{f_2d}")
# Man kann eine Dimension mit einer -1 versehen, diese wird dann automatisch ausgerechnet.
f_2d = f.reshape(-1, 1)
print(f"Array f.reshape(-1, 1):\n{f_2d}")


# Aufgabe 5)
# Das was hier passiert nennt sich 'numpy-broadcasting' und ist eine sehr 'mächtiges' feature von numpy arrays.
# Es ist nicht notwendig dieses Feature von Anfang an zu verstehen, es erweißt sich nur irgendwann als
# sehr nützlich.
# Details findest du in der Dokumentation: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html

print("\nAufgabe 5*)")
print("Zum Vergleich noch mal die beiden Summanden:")
print(f"Array e_2d: {e_2d}")
print(f"e_2d.shape: {e_2d.shape}")
print(f"Array f_2d:\n{f_2d}")
print(f"f_2d.shape: {f_2d.shape}")
print(f"Array e_2d + f_2d:\n{e_2d + f_2d}")
