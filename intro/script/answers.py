import pandas as pd
import matplotlib.pyplot as plt
import json
from pprint import pprint
plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif'


def operating_system(answers):
    list = []
    for participant in answers:
        if (participant['toolbox'] == True):
            list.append(participant['os'])
    os = pd.Series(list).value_counts()
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
    list = []
    for participant in answers:
        if (participant['toolbox'] == True):
            list.append(participant['skill'])
    programming = pd.Series(list)
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
    list = []
    for participant in answers:
        if (participant['toolbox'] == True and participant['skill'] != 'Noch nie programmiert'):
            str = ''
            if (participant['languages']['c'] == True):
                str += 'C;'
            if (participant['languages']['cpp'] == True):
                str += 'C++;'
            if (participant['languages']['fortran'] == True):
                str += 'Fortran;'
            if (participant['languages']['haskell'] == True):
                str += 'Haskell;'
            if (participant['languages']['java'] == True):
                str += 'Java;'
            if (participant['languages']['javascript'] == True):
                str += 'JavaScript;'
            if (participant['languages']['pascal'] == True):
                str += 'Pascal;'
            if (participant['languages']['python'] == True):
                str += 'Python;'
            if (participant['languages']['other'] != ''):
                str += participant['languages']['other'].replace(', ', ';')
                str = str.replace('#', '\#')
            if (str != ''):
                if (str[-1] == ';'):
                    str = str[:-1]
                list.append(str)
    languages = pd.Series(list)
    counts = pd.Series(languages.str.split(';').sum()).value_counts()

    fig = plt.figure(figsize=(5.5, 3.3))
    ax = fig.add_subplot(1, 1, 1)

    counts.sort_values(ascending=True).plot.barh(ax=ax, color='C1')
    plt.tight_layout(pad=0)
    plt.savefig('build/figures/languages.pdf')


def interests(answers):
    list = []
    for participant in answers:
        if (participant['toolbox'] == True):
            if (participant['toolbox_interests']['cli'] == True):
                list.append('Unix')
            if (participant['toolbox_interests']['git'] == True):
                list.append('Git')
            if (participant['toolbox_interests']['make'] == True):
                list.append('Make')
            if (participant['toolbox_interests']['plotting'] == True):
                list.append('Plots')
            if (participant['toolbox_interests']['python'] == True):
                list.append('Auswerten')
            if (participant['toolbox_interests']['uncertainties'] == True):
                list.append('Auto-Fehlerrechnung')
    interest = pd.Series(list)
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
