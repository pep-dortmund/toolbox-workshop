import pandas as pd
import matplotlib.pyplot as plt
import json

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif'

with open('../intro/data/toolbox2020.json', 'r') as read_file:
    answers = json.load(read_file)

list = []
for participant in answers:
    if (participant['latex'] == True):
        list.append(participant['os'])
os = pd.Series(list).value_counts()
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

list = []
for participant in answers:
    if (participant['latex'] == True):
        list.append(participant['latex_level'])
experience = pd.Series(list)

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

list = []
for participant in answers:
    if (participant['latex'] == True):
        if (participant['latex_interests']['beamer'] == True):
            list.append('Präsentationen ')
        if (participant['latex_interests']['bib'] == True):
            list.append('Literaturverzeichnis')
        if (participant['latex_interests']['math'] == True):
            list.append('Formelsatz')
        if (participant['latex_interests']['text'] == True):
            list.append('Textsatz')
        if (participant['latex_interests']['tikz'] == True):
            list.append('Zeichnungen mit TikZ')
        if (participant['latex_interests']['toc'] == True):
            list.append('Automatische Verzeichnisse')
interest = pd.Series(list)
interest = interest.value_counts()

fig, ax = plt.subplots(1, 1, figsize=(5.5, 3.3))

interest.plot.barh(ax=ax)

fig.tight_layout()
fig.savefig('build/figures/interest.pdf')
