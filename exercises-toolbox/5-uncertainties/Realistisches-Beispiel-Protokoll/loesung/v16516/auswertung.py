import numpy as np

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from scipy.constants import physical_constants


# Kommentar:
# Importiere uncertainties unter dem Namen unc
# Importiere uncertainties.unumpy unter dem Namen unp
# Importiere der Funktionen nominal_values und std_devs
# aus uncertainties.unumpy, unter den kürzeren Namen
# noms respektive stds
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)


# Kommentar:
# Die Dateien im Ordner data enthalten jetzt auch spalten  mit den Unsicherheiten
# für die meisten Messwerte
# Beim Importieren der Daten muss beachtet werden, dass:
# (1) Messgröße und Unsicherheit jeweils eine eigene Variablennamen brauchen.
# Auch hier ist eine konsistente Benennung sinnvoll 
# z.B. l (Messwerte) und l_unc (zugehörige Unsicherheiten)
#
# (2) die Unsicherheitbehafteten Messwerte noch erstellt werden müssen,
# entweder durch unc.ufloat oder druch das unp.uarray


# Länge der schiefen Ebene
l, l_unc = np.genfromtxt("data/Messwerte_Bahn.txt", delimiter=",")/100 # m
l = unc.ufloat(l, l_unc)

# Framerate der Kamera (hat keine Unsicherheit, fps_unc = 0)
fps, fps_unc = np.genfromtxt("data/Messwerte_Kamera.txt", delimiter=",") # 1/s

# Masse und Umfang der Kugel
m_b, m_b_unc, u_b, u_b_unc = np.genfromtxt("data/Messwerte_Kugel.txt", delimiter=",", unpack=True)

m_b = unc.ufloat(m_b,m_b_unc)/1000 # kg
u_b = unc.ufloat(u_b,m_b_unc)/100 # m

# Messreihe: Starthöhe und Startframe und Endframe (Kugel)
h_b, h_b_unc, Fi_b, Fi_b_unc, Ff_b, Ff_b_unc = np.genfromtxt("data/Messwerte_Frames_Kugel.txt", delimiter=",", unpack=True)
h_b = unp.uarray(h_b, h_b_unc)/100 # m
Fi_b = unp.uarray(Fi_b, Fi_b_unc)
Ff_b = unp.uarray(Ff_b, Ff_b_unc)


# Masse und Umfang des Zylinders
m_c, m_c_unc, u_c, u_c_unc, d_c, d_c_unc = np.genfromtxt("data/Messwerte_Zylinder.txt", delimiter=",", unpack=True)
m_c = unc.ufloat(m_c, m_c_unc)/1000 # kg
u_c = unc.ufloat(u_c, u_c_unc)/100 # m
d_c = unc.ufloat(d_c, d_c_unc)/100 # m

# Messreihe: Starthöhe und Startframe und Endframe (Zylinder)
h_c, h_c_unc, Fi_c, Fi_c_unc, Ff_c, Ff_c_unc = np.genfromtxt("data/Messwerte_Frames_Zylinder.txt", delimiter=",", unpack=True)
h_c = unp.uarray(h_c, h_c_unc)/100 # m
Fi_c = unp.uarray(Fi_c, Fi_c_unc)
Ff_c = unp.uarray(Ff_c, Ff_c_unc)



# Kommentar:
# Die folgenden Berechnungen funktionieren alle weiterhin, nur jetzt mit automatischen Fehlerrechnung


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
# Nur für die Erstellung der Plots und Fits ändert sich etwas:
# Weder scipy noch matplotlib können direkt mit den unsicherheitbehafteten
# Messwerten umgehen.
# Folgendes muss dafür geändert werden:
#
# (1) in der Fitfunktien müssen mit der Funktion noms() 
# die Unsicherheiten von Konstanten entfernt werden
#
# (2) mit Unsicherheiten der unabhängigen Variable kann curve_fit nicht umgehen,
# diese müssen mit noms() entfernt werden.
# 
# (3) die Werte und  Unsicherheiten der abhängigen Variable (gemessene Funktionswerte)
# müssen getrennt übergeben werden: noms() und stds()
#
# (4) die Darstellung der Messwerte im Plot wird durch errorbar() ersetzt, 
# um die Unsicherheiten anzeigen zu können
#
# In der Aufgabe 3-curve_fit muss eine Funktion ucurve_fit geschrieben werden, 
# die die scipy funktion curve_fit verwendet, die aber den umgang mit den 
# Unsicherheiten abstrahiert, sodass man das nicht jedes mal aufs neue machen muss.



def fit_g_ball(h, g, t0):
    return np.sqrt(7/5 * 1/h * 2* noms(l)**2/g) + t0

def fit_g_cylinder(h, g, t0):
    return np.sqrt((3 + noms(ri_c**2/ro_c**2)) * noms(l)**2/g * 1/h) + t0


params, covariance_matrix = curve_fit(fit_g_ball, noms(h_b_mean), noms(t_b_mean), sigma=stds(t_b_mean))
param_uncertainties = np.sqrt(np.diag(covariance_matrix))


print("Fitparameter (Kugel)")
for name, value, uncertainty in zip("gt", params, param_uncertainties):
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")
print("\n")


h_plot = np.linspace(0.03, 0.33, 205)


# Fit Parameter für den Zylinder


fig, ax = plt.subplots(1, 1, layout="constrained")


ax.set_xlabel("$h$ / m")
ax.set_ylabel("$t$ / s")



ax.errorbar(noms(h_b_mean), noms(t_b_mean), yerr=stds(h_b_mean), fmt="k+", label="Daten: Kugel")
ax.plot(h_plot, fit_g_ball(h_plot, *params),  label="Fit")
ax.legend()
fig.savefig("plot-g_kugel.pdf")




# Berechnung der Fitparameter für den Zylinder
params, covariance_matrix = curve_fit(fit_g_cylinder, noms(h_c_mean), noms(t_c_mean), sigma=stds(t_c_mean))
param_uncertainties = np.sqrt(np.diag(covariance_matrix))


print("Fitparameter (Zylinder)")
for name, value, uncertainty in zip("gt", params, param_uncertainties):
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")
print("\n")


fig, ax = plt.subplots(1, 1, layout="constrained")

ax.set_xlabel("$h$ / m")
ax.set_ylabel("$t$ / s")


ax.errorbar(noms(h_c_mean), noms(t_c_mean), yerr=stds(h_c_mean), fmt="k+", label="Daten: Zylinder")
ax.plot(h_plot, fit_g_cylinder(h_plot, *params),  label="Fit")
ax.legend()
fig.savefig("plot-g_zylinder.pdf")




def fit_I_ball(h, I, t0):
    g = physical_constants["standard acceleration of gravity"][0]
    return np.sqrt(2/g * 1/h * noms(l)**2 * (1 + I/(noms(m_b * r_b)**2)) ) + t0


def fit_I_cylinder(h, I, t0):
    g = physical_constants["standard acceleration of gravity"][0]
    return np.sqrt(2/g * 1/h * noms(l)**2 * (1 + I/(noms(m_c * ro_c**2)) )) + t0


# Berechnung der Fitparameter für die Kugel
params, covariance_matrix = curve_fit(fit_I_ball, noms(h_b_mean), noms(t_b_mean), sigma=stds(t_b_mean))
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


ax.errorbar(noms(h_b_mean), noms(t_b_mean), yerr=stds(h_b_mean), fmt="k+", label="Daten: Kugel")
ax.plot(h_plot, fit_I_cylinder(h_plot, *params),  label="Fit")
ax.legend()
fig.savefig("plot-I_kugel.pdf")


# Berechnung der Fitparameter für den Zylinder
params, covariance_matrix = curve_fit(fit_I_cylinder, noms(h_c_mean), noms(t_c_mean), sigma=stds(t_c_mean))
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


ax.errorbar(noms(h_c_mean), noms(t_c_mean), yerr=stds(h_c_mean), fmt="k+", label="Daten: Zylinder")
ax.plot(h_plot, fit_I_cylinder(h_plot, *params),  label="Fit")
ax.legend()
fig.savefig("plot-I_zylinder.pdf")
