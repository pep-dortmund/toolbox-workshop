import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(
    './FB53-Coronafallzahlen.csv',
    delimiter=';',
    names=True, # column names from first row,
    encoding='utf-8-sig', # the file has a BOM,
    dtype=None,  # guess dtypes (keeps Datum a str and the rest integer),
    missing_values='-',    # missing value indicator
)

spalten = data.dtype.names

plt.bar(data['Datum'], data['Zuwachs_positiver_Testergebnisse_zum_Vortag'], label='Positive Fälle')
liste = np.array([])
dortmund = 6.03609
rki = 5.88250
for i in range(data['Datum'].size - 7):
    liste = np.append(liste, np.sum(data['Zuwachs_positiver_Testergebnisse_zum_Vortag'][i:i+7].astype(int)))
plt.plot(data['Datum'][7:], liste/dortmund, 'y.', markersize=3, label='7-Tage Inzidenz Do')
plt.plot(data['Datum'][7:], liste/rki, 'r.', markersize=3, label='7-Tage Inzidenz RKI')
plt.legend()
plt.xticks(data['Datum'][::14], data['Datum'][::14], rotation=90)
plt.xlim(-1, data['Datum'].size)
plt.tight_layout()
plt.savefig('loesung-faelle-pro-tag.pdf')
plt.clf()

plt.bar(data['Datum'], data['positive_Testergebnisse_insgesamt'].astype(int), label='Fälle gesamt')
plt.bar(data['Datum'], data['genesene_Personen_gesamt'].astype(int), label='Genesene gesamt')
plt.bar(data['Datum'], data['ursächlich_an_COVID19_Verstorbene'].astype(int), label='Verstorbene gesamt')
plt.bar(data['Datum'], data['aufgrund_anderer_Ursachen_Verstorbene'].astype(int), label='andere Verstorbene gesamt')
plt.legend()
plt.xticks(data['Datum'][::14], data['Datum'][::14], rotation=90)
plt.xlim(-1, data['Datum'].size)
plt.tight_layout()
plt.savefig('loesung-insgesamt.pdf')
plt.clf()

plt.bar(data['Datum'], data['aktuell_erkrankte_Personen'].astype(int), label='erkrankt')
plt.bar(data['Datum'], data['darunter_aktuell_stationär_behandelte_Personen'].astype(int), label='stationär')
plt.bar(data['Datum'], data['darunter_aktuell_intensivmedizinisch_behandelte_Personen'].astype(int), label='intensiv')
plt.bar(data['Datum'], data['darunter_aktuell_beatmete_Personen'].astype(int), label='beatmet')
plt.legend()
plt.xticks(data['Datum'][::14], data['Datum'][::14], rotation=90)
plt.xlim(-1, data['Datum'].size)
plt.tight_layout()
plt.savefig('loesung-aktuell.pdf')
plt.clf()
