import numpy as np

import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.style import use
use('ggplot')

colors = [
    '#D0583A',
    '#7777CD',
    '#7FBC3B',
    '#CC52B0',
]

answers = pd.read_csv('data/answers.tsv', sep='\t')

os = answers['Betriebssystem'].value_counts()
os /= os.sum()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0, 0, 0.75, 1])
ax.pie(os.values, labels=os.keys(), colors=colors, startangle=-10)
fig.savefig('build/figures/os.pdf')

programming = answers['Programmierkenntnisse']

programming[programming == 'in einer Sprache außer Python programmiert (z.B. in EINP/DAP)'] = 'programmiert'
programming[programming == 'bereits in Python programmiert'] = 'Python'

programming = programming.value_counts()
programming /= programming.sum()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0.0, 0.0, 0.75, 1])
ax.pie(programming.values, labels=programming.keys(), colors=colors)
fig.savefig('build/figures/programming.pdf')

interest = answers['Mich interessieren besonders']
i = []
for foo in interest:
    if not isinstance(foo, str):
        continue
    i += foo.split(', ')
interest = pd.Series(i)

interest[interest == 'Umgang mit der Kommandozeile (bash)'] = 'Unix'
interest[interest == 'Auswerten mit einer richtigen Programmiersprache (Python+numpy+scipy)'] = 'NumPy'
interest[interest == 'Vernünftige Plots erstellen (Python+matplotlib)'] = 'matplotlib'
interest[interest == 'Automatisierung von Fehlerrechnung (Python+uncertainties+sympy)'] = 'uncertainties'
interest[interest == 'Protokolle automatisiert und reproduzierbar erstellen (make)'] = 'make'
interest[interest == 'Zusammenarbeit mittels Versionskontrolle (git)'] = 'git'

interest = interest.value_counts()

fig, ax = plt.subplots(1, 1)
pos = np.arange(len(interest))
ax.barh(pos, interest.values, align='center')
ax.set_yticklabels([''] + list(interest.keys()))
fig.tight_layout()
fig.savefig('build/figures/interest.pdf')
