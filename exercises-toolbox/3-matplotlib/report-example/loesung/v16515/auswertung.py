import numpy as np
# Kommentar:
# Importiere matplotlib.pyplot unter dem Namen plt

import matplotlib.pyplot as plt

# Länge der schiefen Ebene
l = np.genfromtxt("data/Messwerte_Bahn.txt", delimiter=",")/100 # m

# Framerate der Kamera
fps = np.genfromtxt("data/Messwerte_Kamera.txt", delimiter=",") # 1/s

# Masse und Umfang der Kugel
m_b, u_b = np.genfromtxt("data/Messwerte_Kugel.txt", delimiter=",", unpack=True)
m_b = m_b/1000 # kg
u_b = u_b/100 # m

# Messreihe: Starthöhe und Startframe und Endframe (Kugel)
h_b, Fi_b, Ff_b = np.genfromtxt("data/Messwerte_Frames_Kugel.txt", delimiter=",", unpack=True)
h_b = h_b/100 # m

# Masse und Umfang des Zylinders
m_c, u_c, d_c = np.genfromtxt("data/Messwerte_Zylinder.txt", delimiter=",", unpack=True)
m_c = m_c/1000 # kg
u_c = u_c/100 # m
d_c = d_c/100 # m

# Messreihe: Starthöhe und Startframe und Endframe (Zylinder)
h_c, Fi_c, Ff_c = np.genfromtxt("data/Messwerte_Frames_Zylinder.txt", delimiter=",", unpack=True)
h_c = h_c/100 # m


# Berechnung der benötigten Größen: Radius und Trägheitsmoment

# Radius der Kugel
r_b = u_b/(2*np.pi)

# Äußerer Radius des Zylinders
ro_c = u_c/(2*np.pi)

# Innerer Radius des Zylinders
ri_c = ro_c - d_c


# Trägheitsmoment der Kugel
I_b = 2/5 * m_b * r_b**2

# Trägheitsmoment des Zylinders
I_c = 1/2 * m_c * (ro_c**2 + ri_c**2)

print("Trägheitsmoment (Kugel)")
print(I_b)

print("Trägheitsmoment (Zylinder)")
print(I_c)


# Berechnung der Rollzeiten aus den Messwerten der Frames und Framerate
t_b = (Ff_b - Fi_b)/fps
t_c = (Ff_c - Fi_c)/fps

# Berechnung des Mittelwerts für die Zeitdauer t für jede (dreifach gemessene) Höhe 

t_b_mean = t_b.reshape(-1,3).mean(axis=1)
h_b_mean = h_b.reshape(-1,3)[:,0]
t_c_mean = t_c.reshape(-1,3).mean(axis=1)
h_c_mean = h_c.reshape(-1,3)[:,0]

# Ausgabe verarbeiteten der Messwerte

print("Messwerte (Kugel)")
print("alle Zeiten")
print(t_b)
print("alle Höhen")
print(h_b)
print("Höhe")
print(h_b_mean)
print("gemittlelte Zeit")
print(t_b_mean)
print("\n")


print("Messwerte (Zylinder)")
print("alle Höhen")
print(h_c)
print("alle Zeiten")
print(t_c)
print("Höhe")
print(h_c_mean)
print("gemittlelte Zeit")
print(t_c_mean)


# Erstelle Plots der Messwerte t_._mean und h_._mean

# Kommentar:
# Funktionen für die Funktionsgleichungen der Theoriekurven
# In Funktionen können Variablen verwendet werden, die außerhalb (global) definiert wurden
# wie hier: l, ri_c und ro_c 
# Solche golbalen Variablen können bei größeren Skripten/Programmen zu einem Problem werden
# es ist also zumindest Vorsicht geboten

def theory_t_ball(h):
     return np.sqrt(7/5 * 1/h * 2* l**2/9.81)

def theory_t_cylinder(h):
    return np.sqrt((3 + ri_c**2/ro_c**2) * l**2/9.81 * 1/h)

# Kommentar:
# Die Werte für h die im Plot der Theoriekurven verwendet werden, damit diese 
# auch tatsächlich aussieht wie eine differenzierbare Funktion
# Der Bereich in dem diese Werte liegen entspricht aber dem der Messwerte ca. [0.03, 0.33]

h_plot = np.linspace(0.03, 0.33, 205)


# Kommentar:
# Erstellen einer figure mit einem subplot darin (1 Zeile x 1 Spalte an subplots)

fig, ax = plt.subplots(1, 1, layout="constrained")

# Kommentar:
# Einstellung der Achsenbeschriftungen

ax.set_xlabel("$h$ / m")
ax.set_ylabel("$t$ / s")


ax.plot(h_b_mean, t_b_mean, "k+", label="Daten: Kugel")
# Kommentar:
# Darstellen der Messwerte mit Legendeneintrag
ax.plot(h_plot, theory_t_ball(h_plot),  label="Theorie")
ax.legend()
fig.savefig("plot_kugel.pdf")



# Kommentar:
# Erstellen einer figure mit einem subplot darin (1 Zeile x 1 Spalte an subplots)

fig, ax = plt.subplots(1, 1, layout="constrained")

# Kommentar:
# Einstellung der Achsenbeschriftungen

ax.set_xlabel("$h$ / m")
ax.set_ylabel("$t$ / s")

# Kommentar:
# Darstellen der Messwerte mit Legendeneintrag

ax.plot(h_c_mean, t_c_mean, "k+", label="Daten: Zylinder")
ax.plot(h_plot, theory_t_cylinder(h_plot),  label="Theorie")
ax.legend()
fig.savefig("plot_zylinder.pdf")

