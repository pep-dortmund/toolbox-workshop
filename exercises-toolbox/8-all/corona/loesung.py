import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(
    "./FB53-Coronafallzahlen.csv",
    delimiter=";",
    names=True,  # column names from first row,
    encoding="utf-8-sig",  # the file has a BOM,
    dtype=None,  # guess dtypes (keeps Datum a str and the rest integer),
    missing_values="-",  # missing value indicator
)

spalten = data.dtype.names

dortmund = 6.03609
rki = 5.88250
n_positive_tests = np.convolve(
    data["Zuwachs_positiver_Testergebnisse_zum_Vortag"], np.ones(7)
)[:-6]

fig, ax = plt.subplots(1, 1, constrained_layout=True)

ax.bar(
    data["Datum"],
    data["Zuwachs_positiver_Testergebnisse_zum_Vortag"],
    label="Positive Fälle",
)

ax.plot(
    data["Datum"],
    n_positive_tests / dortmund,
    "k.",
    markersize=3,
    label="7-Tage Inzidenz Do",
)
ax.plot(
    data["Datum"],
    n_positive_tests / rki,
    "c.",
    markersize=3,
    label="7-Tage Inzidenz RKI",
)

ax.plot([-1, data["Datum"].size], [35, 35], "-g", linewidth=0.5)
ax.plot([-1, data["Datum"].size], [50, 50], "-y", linewidth=0.5)
ax.plot([-1, data["Datum"].size], [75, 75], "-r", linewidth=0.5)

fig.suptitle(
    "Fälle pro Tag mit 7-Tage-Inzidenz, \n Stadt Dortmund: "
    + r"$\num{603609}$ Einwohner, RKI: $\num{588250}$ Einwohner"
)
ax.legend(loc="upper center")
ax.set_xticks(data["Datum"][::14], data["Datum"][::14], rotation=90)
ax.set_xlim(-1, data["Datum"].size)
fig.savefig("build/loesung-faelle-pro-tag.pdf")
ax.cla()

ax.plot(
    data["Datum"],
    n_positive_tests / dortmund,
    "k.",
    markersize=3,
    label="7-Tage Inzidenz Do",
)
ax.plot(
    data["Datum"],
    n_positive_tests / rki,
    "c.",
    markersize=3,
    label="7-Tage Inzidenz RKI",
)

ax.plot([-1, data["Datum"].size], [35, 35], "-g", linewidth=0.5)
ax.plot([-1, data["Datum"].size], [50, 50], "-y", linewidth=0.5)
ax.plot([-1, data["Datum"].size], [75, 75], "-r", linewidth=0.5)

fig.suptitle(
    "7-Tage-Inzidenz, \n Stadt Dortmund: "
    + r"$\num{603609}$ Einwohner, RKI: $\num{588250}$ Einwohner"
)
ax.legend(loc="upper center")
ax.set_xticks(data["Datum"][::14], data["Datum"][::14], rotation=90)
ax.set_xlim(-1, data["Datum"].size)
ax.set_ylim(0, np.max(n_positive_tests / rki) * 1.05)
fig.savefig("build/loesung-inzidenz.pdf")
ax.cla()

fig.suptitle("Gesamtzahl an Fällen")
ax.bar(
    data["Datum"], data["positive_Testergebnisse_insgesamt"], label="positive Tests"
)
ax.bar(data["Datum"], data["genesene_Personen_gesamt"], label="Genesene")
ax.bar(
    data["Datum"],
    50 * data["ursächlich_an_COVID19_Verstorbene"],
    label=r"Verstorbene $\cdot 50$",
)
ax.bar(
    data["Datum"],
    50 * data["aufgrund_anderer_Ursachen_Verstorbene"],
    label=r"an anderer Ursache Verstorbene $\cdot 50$",
)
ax.legend()
ax.set_xticks(data["Datum"][::14], data["Datum"][::14], rotation=90)
ax.set_xlim(-1, data["Datum"].size)
ax.set_ylim(0, np.max(data["positive_Testergebnisse_insgesamt"]) * 1.05)
fig.savefig("build/loesung-insgesamt.pdf")
ax.cla()

fig.suptitle("Aktuelle Fälle pro Tag")
ax.bar(data["Datum"], data["aktuell_erkrankte_Personen"], label="erkrankt")
ax.bar(
    data["Datum"],
    data["darunter_aktuell_stationär_behandelte_Personen"],
    label="stationär",
)
ax.bar(
    data["Datum"],
    data["darunter_aktuell_intensivmedizinisch_behandelte_Personen"],
    label="intensiv",
)
ax.bar(data["Datum"], data["darunter_aktuell_beatmete_Personen"], label="beatmet")
ax.legend()
ax.set_xticks(data["Datum"][::14], data["Datum"][::14], rotation=90)
ax.set_xlim(-1, data["Datum"].size)
ax.set_ylim(0, np.max(data["aktuell_erkrankte_Personen"]) * 1.05)
fig.savefig("build/loesung-aktuell.pdf")
fig.clf()
