import pandas as pd
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

fig = plt.figure(figsize=(4, 3))
ax = fig.add_axes([0, 0, 0.75, 1])
ax.pie(os.values, labels=os.keys(), colors=colors, startangle=-10)
fig.savefig('build/figures/os.pdf')

experience = answers['Erfahrung mit LaTeX']

experience = experience.value_counts()
experience /= experience.sum()

fig = plt.figure(figsize=(4, 3))
ax = fig.add_axes([0.0, 0.0, 0.75, 1])
ax.pie(experience.values, labels=experience.keys(), colors=colors)
fig.savefig('build/figures/experience.pdf')
