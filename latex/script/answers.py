import pandas as pd
import matplotlib.pyplot as plt
import json

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif'

with open('../intro/data/toolbox2022.json', 'r') as read_file:
    answers = json.load(read_file)

liste = []
for participant in answers:
    if participant['latex'] is True:
        liste.append(participant['os'])
os = pd.Series(liste).value_counts()
os /= os.sum()

fig = plt.figure(figsize=(5.3, 3.3))
ax = fig.add_axes([0, 0, 1, 1], aspect=1)
ax.pie(
    os.values,
    labels=os.index,
    startangle=-10,
    radius=1,
    center=(0, 0),
)
ax.set_xlim(-1, 2)
fig.savefig('build/figures/os.pdf')

liste = []
for participant in answers:
    if participant['latex'] is True:
        liste.append(participant['latex_level'])
experience = pd.Series(liste)

experience = experience.value_counts()
experience /= experience.sum()

fig = plt.figure(figsize=(5.3, 3.3))
ax = fig.add_axes([0, 0, 1, 1], aspect=1)
ax.pie(
    experience.values,
    labels=experience.index,
    radius=1,
)
ax.set_xlim(-1, 2)
fig.savefig('build/figures/experience.pdf')

liste = []
for participant in answers:
    if participant['latex'] is True:
        for topic, interest in participant['latex_interests'].items():
            if interest:
                liste.append(topic)
interest = pd.Series(liste)
interest.replace(
    {
        'beamer': 'Präsentationen',
        'bib': 'Literaturverzeichnis',
        'math': 'Formelsatz',
        'text': 'Textsatz',
        'tikz': 'Zeichnungen mit TikZ',
        'toc': 'Automatische Verzeichnisse'
    },
    inplace=True
)
interest = interest.value_counts()

fig, ax = plt.subplots(1, 1, figsize=(5.5, 3.3))

interest.plot.barh(ax=ax)

fig.tight_layout()
fig.savefig('build/figures/interest.pdf')
