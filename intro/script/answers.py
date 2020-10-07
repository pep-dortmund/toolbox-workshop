import pandas as pd
import matplotlib.pyplot as plt
import json
from pprint import pprint
plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif'


def operating_system(answers):
    liste = []
    for participant in answers:
        if participant['toolbox'] is True:
            liste.append(participant['os'])
    os = pd.Series(liste).value_counts()
    os /= os.sum()

    fig = plt.figure(figsize=(5.5, 3.3))
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.pie(
        os.values,
        labels=os.keys(),
        startangle=-10,
        radius=1,
    )
    ax.set_xlim(-1.3, 2)
    fig.savefig('build/figures/os.pdf')


def programming(answers):
    liste = []
    for participant in answers:
        if participant['toolbox'] is True:
            liste.append(participant['skill'])
    programming = pd.Series(liste)
    programming = programming.str.replace(',', ',\n')

    programming = programming.value_counts()
    programming /= programming.sum()

    fig = plt.figure(figsize=(5.5, 3.3))
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.pie(
        programming.values,
        labels=programming.keys(),
        startangle=0,
        radius=1,
    )
#    ax.set_xlim(-1.5, 1.5)
    fig.savefig('build/figures/programming.pdf')


def languages(answers):
    liste = []
    for participant in answers:
        if participant['toolbox'] is True:
            for language, answer in participant['languages'].items():
                if answer and language == 'other':
                    answer = answer.replace(', ', ';')
                    answer = answer.replace('#', '\#')
                    liste.append(answer)
                if answer:
                    liste.append(language)
    languages = pd.Series(liste)
    languages.replace(
        {
            'c': 'C',
            'cpp': 'C++',
            'fortran': 'Fortran',
            'haskell': 'Haskell',
            'java': 'Java',
            'javascript': 'JavaScript',
            'pascal': 'Pascal',
            'python': 'Python'
        },
        inplace=True
    )
    counts = pd.Series(languages.str.split(';').sum()).value_counts()

    fig = plt.figure(figsize=(5.5, 3.3))
    ax = fig.add_subplot(1, 1, 1)

    counts.sort_values(ascending=True).plot.barh(ax=ax, color='C1')
    plt.tight_layout(pad=0)
    plt.savefig('build/figures/languages.pdf')


def interests(answers):
    liste = []
    for participant in answers:
        if participant['toolbox'] is True:
            for topic, interest in participant['toolbox_interests'].items():
                if interest:
                    liste.append(topic)
    interest = pd.Series(liste)
    interest.replace(
        {
            'cli': 'Unix',
            'git': 'Git',
            'make': 'Make',
            'plotting': 'Plots',
            'python': 'Auswerten',
            'uncertainties': 'Auto-Fehlerrechnung'
        },
        inplace=True
    )
    interest = interest.value_counts()
    fig, ax = plt.subplots(1, 1, figsize=(5.5, 3.3))

    interest.plot.barh(ax=ax)

    fig.tight_layout()
    fig.savefig('build/figures/interest.pdf')


if __name__ == '__main__':
    with open('data/toolbox2020.json', 'r') as read_file:
        data = json.load(read_file)
    languages(data)
    operating_system(data)
    programming(data)
    interests(data)
