# Kommentar:
# Importiere numpy unter dem Namen np

import numpy as np

# Kommentar:
# Die Daten liegen im Ordner 'data'. Um die Dateien einlesen
# zu können reicht es deswegen nicht den Dateinamen anzugeben
# es muss der gesamte Pfad ('Orderabfolge') angegeben werden: 
# 
# Für die Datei: Messwerte_Bahn.txt also data/Messwerte_Bahn.txt
#
# Der Name der Variable in der die eingelesenen Werte gespeichert werden
# ist frei wählbar, es bietet sich bei 'langen' Skripten an (im Gegensatz zur Mathematik)
# nicht nur einbuchstabige Abkürzungen zu verwenden, um nicht die Übersicht zu verlieren.
# Also beispielsweise track_length statt L. Ein Kommentar zur erklären sollte aber drin sein.
#
# Es bietet sich an die Daten direkt beim einlesen in eine sinnvolle Einheit umzuwandeln
# (falls nötig) und diese mit einem Kommentar zu vermerken

# Länge der schiefen Ebene
L = np.genfromtxt("data/Messwerte_Bahn.txt", delimiter=",")/100 # m

# Framerate der Kamera
fps = np.genfromtxt("data/Messwerte_Kamera.txt", delimiter=",") # 1/s
# Kommentar:
# Die Daten aus Dateien mit mehreren spalten muss man in einer extra Zeile skalieren

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

# Kommentar:
# Eine gewisses Maß an Struktur in der Benennung von Variablen hilft bei der Orientierung,
# garade in der Zusammenarbeit mit euren jeweiligen Partnern.
# Man muss es aber auch nicht übertreiben. Gerade ein Sprachenmix aus deutsch und englisch
# ist nicht besonders tragisch: z.B. steht m_b für mass_ball aber u_b für umfang_ball,
# aber das p_b für perimeter_ball würde mir persönlich nicht so klar werden. 


# Kommentar:
# Auch die einzelnen "Arbeitsschritte" der Auswertung sollten in einem
# kurzen Kommentar erklärt werden.

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

print("Messwerte (Ball)")
print("Zeit")
print(t_b)

print("Höhe")
print(h_b)
print("\n")
print("Messwerte (Zylinder)")
print("Zeit")
print(t_c)
print("Höhe")
print(h_c)



