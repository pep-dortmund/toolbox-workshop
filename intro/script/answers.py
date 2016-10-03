import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif'

colors = [
    '#D0583A',
    '#7777CD',
    '#7FBC3B',
    '#CC52B0',
    'yellow',
]

answers = pd.read_csv('data/2016.csv')

os = answers['Betriebssystem'].value_counts()
os /= os.sum()

fig = plt.figure(figsize=(4, 3))
ax = fig.add_axes([0.125, 0, 0.75, 1], aspect=1)
ax.pie(os.values, labels=os.keys(), colors=colors, startangle=-10)
fig.savefig('build/figures/os.pdf')

programming = answers['Programmierkentnisse']
programming = programming.str.replace(',', ',\n')

programming = programming.value_counts()
programming /= programming.sum()

fig = plt.figure(figsize=(4, 3))
ax = fig.add_axes([0.125, 0.0, 0.75, 1], aspect=1)
ax.pie(
    programming.values,
    labels=programming.keys(),
    colors=colors,
    startangle=0,
    radius=1,
    labeldistance=0.4,
    textprops={
        'va': 'center',
        'ha': 'center',
        'bbox': {'facecolor': 'w', 'alpha': 0.6},
    },
)
fig.savefig('build/figures/programming.pdf')

interest = pd.Series([
    elem
    for row in answers['Mich interessiert besonders'].str.split(';')
    for elem in row
])

interest.replace(
    {
        'Umgang mit der Kommandozeile': 'Unix',
        'Zusammenarbeiten / Versionskontrolle mit Git': 'Git',
        'Versuchsauswertung mit Python / Numpy / Scipy': 'Auswerten',
        'Qualitativ hochwertige Plots erstellen mit Matplotlib': 'Plots',
        'Automatisierung/Reproduzierbarkeit mit Make': 'Make',
        'Automatisierung der Fehlerrechnung mit Uncertainties und SymPy': 'Auto-Fehlerrechnung',
    },
    inplace=True,
)

interest = interest.value_counts()

fig, ax = plt.subplots(1, 1, figsize=(4, 3))

interest.plot.barh(ax=ax)

fig.tight_layout()
fig.savefig('build/figures/interest.pdf')
