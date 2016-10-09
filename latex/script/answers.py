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

fig = plt.figure()
ax = fig.add_axes([0.125, 0, 0.75, 1], aspect=1)
ax.pie(os.values, labels=os.keys(), colors=colors, startangle=-10)
fig.savefig('build/figures/os.pdf')

experience = answers['Erfahrung mit LaTeX']

experience = experience.value_counts()
experience /= experience.sum()

fig = plt.figure()
ax = fig.add_axes([0.125, 0.0, 0.75, 1], aspect=1)
ax.pie(experience.values, labels=experience.keys(), colors=colors)
fig.savefig('build/figures/experience.pdf')
