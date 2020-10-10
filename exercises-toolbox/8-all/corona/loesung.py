import numpy as np
import matplotlib.pyplot as plt

Datum, positiver, insgesamt, genesene, Verstorbene, anderer_Verstorbene, aktuell_erkrankte, aktuell_stationaer, aktuell_intensiv, aktuell_beatmete = np.genfromtxt('FB53-Coronafallzahlen.csv', delimiter=';', unpack=True, dtype='U', skip_header=1)

for x in [positiver, insgesamt, genesene, Verstorbene, anderer_Verstorbene, aktuell_erkrankte, aktuell_stationaer, aktuell_intensiv, aktuell_beatmete]:
    x[x == '-'] = '0'
    x[x == ''] = '0'

plt.bar(Datum, positiver.astype(int), label='Positive Fälle')
liste = []
for i in range(Datum.size - 7):
    liste.append(np.mean(positiver[i:i+7].astype(int)))
plt.plot(Datum[7:], liste, 'r.', markersize=3, label='7-Tage Inzidenz')
plt.legend()
plt.xticks(Datum[::10], Datum[::10], rotation=90)
plt.xlim(-1, Datum.size)
plt.tight_layout()
plt.savefig('loesung-faelle-pro-tag.pdf')
plt.clf()

plt.bar(Datum, insgesamt.astype(int), label='Fälle gesamt')
plt.bar(Datum, genesene.astype(int), label='Genesene gesamt')
plt.bar(Datum, Verstorbene.astype(int), label='Verstorbene gesamt')
plt.bar(Datum, anderer_Verstorbene.astype(int), label='andere Verstorbene gesamt')
plt.legend()
plt.xticks(Datum[::10], Datum[::10], rotation=90)
plt.xlim(-1, Datum.size)
plt.tight_layout()
plt.savefig('loesung-insgesamt.pdf')
plt.clf()

plt.bar(Datum, aktuell_erkrankte.astype(int), label='erkrankt')
plt.bar(Datum, aktuell_stationaer.astype(int), label='stationär')
plt.bar(Datum, aktuell_intensiv.astype(int), label='intensiv')
plt.bar(Datum, aktuell_beatmete.astype(int), label='beatmet')
plt.legend()
plt.xticks(Datum[::10], Datum[::10], rotation=90)
plt.xlim(-1, Datum.size)
plt.tight_layout()
plt.savefig('loesung-aktuell.pdf')
plt.clf()
