# 1.
# begin solution
t = 0.5
h_i = 10
v_i = 0.75
a_i = -9.81
# end solution
# 2.
# begin solution
h = h_i + v_i * t + 1 / 2 * a_i * t**2
v = v_i * t + a_i * t
a = a_i
# end solution
# 3.
# begin solution
h < 9
# end solution
# 4.
# begin solution
print("Start...")
print("...höhe")
print(h_i)
print("...geschwindigkeit")
print(v_i)
print("...beschleunigung")
print(a_i)

print("Nach der Zeit t")
print(t)
print("Höhe")
print(h)
print("Geschwindigkeit")
print(v)
print("Beschleunigung")
print(a)
# end solution
#  5.
# begin solution
T = [0.5, 1, 1.5]
H = []
V = []
A = []

H.append(h_i + v_i * T[0] + 1 / 2 * a_i * T[0] ** 2)
H.append(h_i + v_i * T[1] + 1 / 2 * a_i * T[1] ** 2)
H.append(h_i + v_i * T[2] + 1 / 2 * a_i * T[2] ** 2)

V.append(v_i * T[0] + a_i * T[0])
V.append(v_i * T[1] + a_i * T[1])
V.append(v_i * T[2] + a_i * T[2])

A.append(a_i)
A.append(a_i)
A.append(a_i)

print(H)
print(V)
print(A)
# end solution
# 6.
# begin solution
data = {"t": T, "h": H, "v": V, "a": A}
print(data)
# end solution
# 7.
# begin solution
print(data["t"][1])
print(data["v"][0])
print(data["h"][-1])


# end solution
# 8.
# begin solution
def h(t):
    return h_i + v_i * t + 1 / 2 * a_i * t**2


def v(t):
    return v_i * t + a_i * t


def a(t):
    return a_i


# end solution
# 9.
# begin solution
T = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5]
# ohne Schleife
data = {
    "t": T,
    "h": [h(T[0]), h(T[1]), h(T[2]), h(T[3]), h(T[4]), h(T[5])],
    "v": [v(T[0]), v(T[1]), v(T[2]), v(T[3]), v(T[4]), v(T[5])],
    "a": [a(T[0]), a(T[1]), a(T[2]), a(T[3]), a(T[4]), a(T[5])],
}
print(data)
# mit Schleife
H = []
V = []
A = []
for t in T:
    H.append(h(t))
    V.append(v(t))
    A.append(a(t))
data = {"t": T, "h": H, "v": V, "a": A}
print(data)
# end solution
# 10.
# begin solution
for k, v in data.items():
    print(
        f"{k}"
        + f"  {v[0]:.2f}"
        + f"  {v[1]:.2f}"
        + f"  {v[2]:.2f}"
        + f"  {v[3]:.2f}"
        + f"  {v[4]:.2f}"
        + f"  {v[5]:.2f}"
    )
# Am Dezimaltrennzeichen ausgerichtet
for k, v in data.items():
    string = (
        f"{k}"
        + f"  {v[0]:6.2f}"
        + f"  {v[1]:6.2f}"
        + f"  {v[2]:6.2f}"
        + f"  {v[3]:6.2f}"
        + f"  {v[4]:6.2f}"
        + f"  {v[5]:6.2f}"
    )
    print()
# Noch eine Schleife (List-Comprehension) mehr, erübrigt die Wiederholungen
for key, values in data.items():
    formatted_values = " ".join([f"{v:6.2f}" for v in values])
    print(f"{key}  {formatted_values}")
# end solution
