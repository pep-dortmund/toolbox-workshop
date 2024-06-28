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
    data["zuwachs_positiver_testergebnisse_zum_vortag"], np.ones(7)
)[:-6]

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.bar(
    data["datum"],
    data["zuwachs_positiver_testergebnisse_zum_vortag"],
    label="Positive Fälle",
)

ax.plot(
    data["datum"],
    n_positive_tests / dortmund,
    "k.",
    markersize=3,
    label="7-Tage Inzidenz Do",
)
ax.plot(
    data["datum"],
    n_positive_tests / rki,
    "c.",
    markersize=3,
    label="7-Tage Inzidenz RKI",
)

ax.plot([-1, data["datum"].size], [35, 35], "-g", linewidth=0.5)
ax.plot([-1, data["datum"].size], [50, 50], "-y", linewidth=0.5)
ax.plot([-1, data["datum"].size], [75, 75], "-r", linewidth=0.5)

fig.suptitle(
    "Fälle pro Tag mit 7-Tage-Inzidenz, \n Stadt Dortmund: "
    + r"$\num{603609}$ Einwohner, RKI: $\num{588250}$ Einwohner"
)
ax.legend(loc="upper center")
ax.set_xticks(data["datum"][::14], data["datum"][::14], rotation=90)
ax.set_xlim(-1, data["datum"].size)
fig.savefig("build/loesung-faelle-pro-tag.pdf")
ax.cla()

ax.plot(
    data["datum"],
    n_positive_tests / dortmund,
    "k.",
    markersize=3,
    label="7-Tage Inzidenz Do",
)
ax.plot(
    data["datum"],
    n_positive_tests / rki,
    "c.",
    markersize=3,
    label="7-Tage Inzidenz RKI",
)

ax.plot([-1, data["datum"].size], [35, 35], "-g", linewidth=0.5)
ax.plot([-1, data["datum"].size], [50, 50], "-y", linewidth=0.5)
ax.plot([-1, data["datum"].size], [75, 75], "-r", linewidth=0.5)

fig.suptitle(
    "7-Tage-Inzidenz, \n Stadt Dortmund: "
    + r"$\num{603609}$ Einwohner, RKI: $\num{588250}$ Einwohner"
)
ax.legend(loc="upper center")
ax.set_xticks(data["datum"][::14], data["datum"][::14], rotation=90)
ax.set_xlim(-1, data["datum"].size)
ax.set_ylim(0, np.max(n_positive_tests / rki) * 1.05)
fig.savefig("build/loesung-inzidenz.pdf")
ax.cla()

fig.suptitle("Gesamtzahl an Fällen")
ax.bar(data["datum"], data["positive_testergebnisse_insgesamt"], label="positive Tests")
ax.bar(data["datum"], data["genesene_personen_gesamt"], label="Genesene")
ax.bar(
    data["datum"],
    50 * data["verstorben_ursachlich_an_covid_19"],
    label=r"Verstorbene $\cdot 50$",
)
ax.bar(
    data["datum"],
    50 * data["verstorben_aufgrund_anderer_ursachen"],
    label=r"an anderer Ursache Verstorbene $\cdot 50$",
)
ax.legend()
ax.set_xticks(data["datum"][::14], data["datum"][::14], rotation=90)
ax.set_xlim(-1, data["datum"].size)
ax.set_ylim(0, np.max(data["positive_testergebnisse_insgesamt"]) * 1.05)
fig.savefig("build/loesung-insgesamt.pdf")
ax.cla()

fig.suptitle("Aktuelle Fälle pro Tag")
ax.bar(data["datum"], data["aktuell_erkrankte_personen"], label="erkrankt")
ax.bar(
    data["datum"],
    data["darunter_aktuell_stationar_behandelte_personen"],
    label="stationär",
)
ax.bar(
    data["datum"],
    data["darunter_aktuell_intensivmedizinisch_behandelte_personen"],
    label="intensiv",
)
ax.bar(data["datum"], data["darunter_aktuell_beatmete_personen"], label="beatmet")
ax.legend()
ax.set_xticks(data["datum"][::14], data["datum"][::14], rotation=90)
ax.set_xlim(-1, data["datum"].size)
ax.set_ylim(0, np.max(data["aktuell_erkrankte_personen"]) * 1.05)
fig.savefig("build/loesung-aktuell.pdf")
fig.clf()
