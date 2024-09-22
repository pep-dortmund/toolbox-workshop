# Kommentar:
# Importiere numpy unter dem Namen np

import numpy as np

# Kommentar:
# Die Daten liegen im Ordner 'data'. Um die Dateien einlesen
# zu können, reicht es deswegen nicht den Dateinamen anzugeben,
# es muss der gesamte Pfad ('Orderabfolge') angegeben werden: 
# 
# Für die Datei: Messwerte_Bahn.txt also data/Messwerte_Bahn.txt
#
# Der Name der Variable in der die eingelesenen Werte gespeichert werden
# ist frei wählbar, es bietet sich bei 'langen' Skripten an (im Gegensatz zur Mathematik)
# nicht nur einbuchstabige Abkürzungen zu verwenden, um nicht die Übersicht zu verlieren.
# Also beispielsweise track_length statt L. Ein Kommentar zur erklären sollte aber drin sein.
#
# Es bietet sich an die Daten direkt beim Einlesen in eine sinnvolle Einheit umzuwandeln
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
# Ein gewisses Maß an Struktur in der Benennung von Variablen hilft bei der Orientierung,
# gerade in der Zusammenarbeit mit euren jeweiligen Partnern.
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

# Berechnung des Mittelwerts für die Zeitdauer t für jede (dreifach gemessene) Höhe 

# Kommentar:
# Es ist ein neuer Name (t_b_mean) notwendig, wenn die alten Werte in t_b
# noch verfügbar bleiben sollen
#
# Hieran sieht man (schon im Kleinen) die Nützlichkeit der numpy arrays 
# und der möglichen Manipulationen:
# reshape(-1,3):
# Im array t_b liegen die zu mittelnden Werte immer genau hintereinander
# durch reshape(-1,3) wird aus t_b ein 2D array erzeugt, das in jeder 
# Zeile 3 Spalten hat. Das bedeutet: Nach jeweils 3 Werten in t_b wird eine neue
# Zeile begonnen, damit sind in jeder Zeile genau die Werte die gemittelt werden sollen.
# Die -1 als Anzahl der Zeilen ist gibt numpy die Anweisung, diese Anzahl
# selbst zu berechnen.
#
# mean(axis=1):
# Bei einem 2D array bezeichnet axis=0 die Zeilen und axis=1 die Spalten.
# Berechnet den Mittelwert "entlang der axis 1", d.h. die axis 1 ist die "Dimension"
# des arrays, über die summiert wird (die danach nur noch einen Wert enthält).
# Da jede Zeile genau die drei Werte enthält, die zu mitteln sind, enthält jede 
# Zeile danach genau den jeweiligen Mittelwert.

t_b_mean = t_b.reshape(-1,3).mean(axis=1)



# Kommentar:
# Das Array h_b enthält jede Höhe dreifach, auch die Auswahl
# der einzelnen Höhen kann durch array Manipulation geschehen.
#
# Die Benennung der Variable (h_b_mean) wurde so gewählt,
# dass diese zur zugehörigen Variable für die Zeitdauern passt
#
# reshape(-1, 3): 
# analog zur Manipulation von t_b
# [:,0]
# Aus jeder Zeile (= erster Index ist ':') wird die 'nullte' Spalte (= zweiter Index ist '0')
# ausgewählt, d.h. in jeder Zeile bleibt genau eine Höhe erhalten.

h_b_mean = h_b.reshape(-1,3)[:,0]



# Kommentar:
# analog für die andere Messreihe

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
