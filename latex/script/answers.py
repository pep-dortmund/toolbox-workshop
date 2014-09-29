import numpy as np

import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

answers = pd.read_csv('data/answers.tsv', sep='\t')

os = answers['Betriebssystem'].value_counts()
os /= os.sum()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0, 0, 0.75, 1])
ax.pie(os.values, labels=os.keys())
fig.savefig('build/figures/os.pdf')

experience = answers['Erfahrung mit LaTeX']

experience = experience.value_counts()
experience /= experience.sum()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0.0, 0.0, 0.75, 1])
ax.pie(experience.values, labels=experience.keys())
fig.savefig('build/figures/experience.pdf')
