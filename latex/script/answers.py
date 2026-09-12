import json

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("ggplot")
plt.rcParams["font.family"] = "sans-serif"

with open("../intro/data/toolbox2026.json") as read_file:
    answers = json.load(read_file)

liste = []
for participant in answers:
    if participant["latex"] is True:
        liste.append(participant["os"])
os = pd.Series(liste).value_counts()
os /= os.sum()

fig, ax = plt.subplots(
    figsize=(5.3, 3.3), layout="constrained", subplot_kw={"aspect": 1}
)
ax.pie(
    os.values,
    labels=os.index,
    startangle=20,
    radius=1,
    center=(0, 0),
)
ax.set_xlim(-1, 2)
fig.savefig("build/figures/os.pdf")
plt.close(fig=fig)

liste = []
for participant in answers:
    if participant["latex"] is True:
        liste.append(participant["latex_level"])
experience = pd.Series(liste)

mask = experience.str.contains("Facharbeit")
experience.loc[mask] = experience.loc[mask].str.replace("(", "\n(")

experience = experience.value_counts()
experience /= experience.sum()

fig, ax = plt.subplots(
    figsize=(5.3, 3.3), layout="constrained", subplot_kw={"aspect": 1}
)
ax.pie(
    experience.values,
    labels=experience.index,
    radius=1,
)
ax.set_xlim(-1, 2)
fig.savefig("build/figures/experience.pdf")
plt.close(fig=fig)

liste = []
for participant in answers:
    if participant["latex"] is True:
        for topic, interest in participant["latex_interests"].items():
            if interest:
                liste.append(topic)
interest = pd.Series(liste)
interest.replace(
    {
        "beamer": "Präsentationen",
        "bib": "Literaturverzeichnis",
        "math": "Formelsatz",
        "text": "Textsatz",
        "tikz": "Zeichnungen mit TikZ",
        "toc": "Automatische Verzeichnisse",
    },
    inplace=True,
)
interest = interest.value_counts()

fig, ax = plt.subplots(figsize=(5.5, 3.3), layout="constrained")
interest.plot.barh(ax=ax)
fig.savefig("build/figures/interest.pdf")
plt.close(fig=fig)
