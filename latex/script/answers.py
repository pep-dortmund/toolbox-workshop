import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif'

answers = pd.read_csv('data/2017.csv')

os = answers['Betriebssystem'].value_counts()
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

experience = answers['Erfahrung mit LaTeX']

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
