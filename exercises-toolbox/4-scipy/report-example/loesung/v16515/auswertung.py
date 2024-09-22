import numpy as np

import matplotlib.pyplot as plt

# Kommentar:
# Importiere curve_fit aus scipy.optimize
from scipy.optimize import curve_fit
from scipy.constants import physical_constants

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
print("\n")

# Erstelle Plots der Messwerte t_._mean und h_._mean


# Kommentar:
# Umwandeln der Theorie-Funktion zu einer Fit-Funktion:
# Die Funktion erhält ein zusätzliches Argument für jeden Fitparameter, hier: g und t0
# diese müssen auch in der Funktion verwendet werden.
#
# Namen sind wie immer beliebig und es gibt nicht "den einen richtigen Namen",
# aber es bietet sich wie immer an sprechende Namen zu verwenden, hier z.B.
# "fit_g_ball" als Abkürzung für "Fitfunktion für den Parameter g aus den Messwerten für die Kugel"

def fit_g_ball(h, g, t0):
    return np.sqrt(7/5 * 1/h * 2* l**2/g) + t0

def fit_g_cylinder(h, g, t0):
    return np.sqrt((3 + ri_c**2/ro_c**2) * l**2/g * 1/h) + t0


# Kommentar:
# Hier ist Vorsicht geboten, da die Fit-Funktion und Messwerte zusammen passen müssen
# an solchen Stellen zahlt sich eine konsistente Benennung aus.
# Berechnung der Fitparameter für die Kugel
params, covariance_matrix = curve_fit(fit_g_ball, h_b_mean, t_b_mean)
param_uncertainties = np.sqrt(np.diag(covariance_matrix))


# Kommentar:
# Ansehnliche Ausgabe der Parameter aufs Terminal
print("Fitparameter (Kugel)")
for name, value, uncertainty in zip("gt", params, param_uncertainties):
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")
print("\n")


h_plot = np.linspace(0.03, 0.33, 205)


# Fit Parameter für den Zylinder


fig, ax = plt.subplots(1, 1, layout="constrained")


ax.set_xlabel("$h$ / m")
ax.set_ylabel("$t$ / s")


# Kommentar:
# Theorie-Funktion durch Fit-Funktion mit Fit-Parametern ersetzen

ax.plot(h_b_mean, t_b_mean, "k+", label="Daten: Kugel")
ax.plot(h_plot, fit_g_ball(h_plot, *params),  label="Fit")
ax.legend()
fig.savefig("plot-g_kugel.pdf")



# Kommentar:
# Analog für die Messreihe des Zylinders
# Achtung! Copy-and-paste ist natürlich gängige Praxis,
# aber alle Variablen müssen angepasst werden.

# Berechnung der Fitparameter für den Zylinder
params, covariance_matrix = curve_fit(fit_g_cylinder, h_c_mean, t_c_mean)
param_uncertainties = np.sqrt(np.diag(covariance_matrix))


print("Fitparameter (Zylinder)")
for name, value, uncertainty in zip("gt", params, param_uncertainties):
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")
print("\n")


fig, ax = plt.subplots(1, 1, layout="constrained")

ax.set_xlabel("$h$ / m")
ax.set_ylabel("$t$ / s")


ax.plot(h_c_mean, t_c_mean, "k+", label="Daten: Zylinder")
ax.plot(h_plot, fit_g_cylinder(h_plot, *params),  label="Fit")
ax.legend()
fig.savefig("plot-g_zylinder.pdf")



# Kommentar:
# Verwenden der physikalischen Konstanten aus scipy 
# hier: g
# physical_constants enthält 3er-tuple, der erste Eintrag 
# der tuple ist der Wert der Konstante, deswegen [0]

def fit_I_ball(h, I, t0):
    g = physical_constants["standard acceleration of gravity"][0]
    return np.sqrt(2/g * 1/h * l**2 * (1 + I/(m_b * r_b**2)) ) + t0


def fit_I_cylinder(h, I, t0):
    g = physical_constants["standard acceleration of gravity"][0]
    return np.sqrt(2/g * 1/h * l**2 * (1 + I/(m_c * ro_c**2) )) + t0


# Kommentar:
# Durch den Fit wird diese Warnung auf das Terminal ausgegeben:
# .../v16515/auswertung.py:197: RuntimeWarning: invalid value encountered in sqrt
#  return np.sqrt(2/g * 1/h * l**2 * (1 + I/(m_c * ro_c**2) )) + t0
#
# Diese bedeutet, dass während des Fits negative Werte für I 'ausprobiert' wurden,
# von denen die Wurzel nicht berechnet werden konnte.
# Man kann das verhindern, in dem man die Parameter auf den physikalisch möglichen 
# Bereich einschränkt. Dies tut man mit dem zusätzlichen Parameter bounds für curve_fit,
# hier müsste 
# bounds=([0,-np.inf],[+np.inf,+np.inf])
# als zusätzliches Argument für curve_fit ergänzt werden.
# bounds gibt den minimalen und den maximalen Wert für alle Parameter an,
# und zwar zuerst alle Minima und dann alle Maxima, 
# in diesem konkreten Beispiel steht bounds also für: 0 < I < +np.inf und -np.inf < t0 < +np.inf


# Berechnung der Fitparameter für die Kugel
params, covariance_matrix = curve_fit(fit_I_ball, h_b_mean, t_b_mean)
param_uncertainties = np.sqrt(np.diag(covariance_matrix))


print("Fitparameter (Kugel)")
for name, value, uncertainty in zip("It", params, param_uncertainties):
    # in kg*m² sehr klein, umwandlung zu kg*cm²
    if name == "I":
        value *= 10000 
        uncertainty *= 10000
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")
print("\n")


fig, ax = plt.subplots(1, 1, layout="constrained")

ax.set_xlabel("$h$ / m")
ax.set_ylabel("$t$ / s")


ax.plot(h_c_mean, t_c_mean, "k+", label="Daten: Kugel")
ax.plot(h_plot, fit_I_cylinder(h_plot, *params),  label="Fit")
ax.legend()
fig.savefig("plot-I_kugel.pdf")


# Berechnung der Fitparameter für den Zylinder
params, covariance_matrix = curve_fit(fit_I_cylinder, h_c_mean, t_c_mean)
param_uncertainties = np.sqrt(np.diag(covariance_matrix))


print("Fitparameter (Zylinder)")
for name, value, uncertainty in zip("It", params, param_uncertainties):
    # in kg*m² sehr klein, umwandlung zu kg*cm²
    if name == "I":
        value *= 10000 
        uncertainty *= 10000
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")
print("\n")



fig, ax = plt.subplots(1, 1, layout="constrained")

ax.set_xlabel("$h$ / m")
ax.set_ylabel("$t$ / s")


ax.plot(h_c_mean, t_c_mean, "k+", label="Daten: Zylinder")
ax.plot(h_plot, fit_I_cylinder(h_plot, *params),  label="Fit")
ax.legend()
fig.savefig("plot-I_zylinder.pdf")
