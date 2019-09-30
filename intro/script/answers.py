import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif'


def operating_system(answers):
    os = answers['Betriebssystem'].value_counts()
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
    programming = answers['Programmierkentnisse']
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
    ax.set_xlim(-1.3, 2)
    fig.savefig('build/figures/programming.pdf')


def languages(answers):
    languages = answers['Programmiersprachen'].dropna()

    counts = pd.Series(languages.str.split(';').sum()).value_counts()

    fig = plt.figure(figsize=(5.5, 3.3))
    ax = fig.add_subplot(1, 1, 1)

    counts.sort_values(ascending=True).plot.barh(ax=ax, color='C1')
    fig.tight_layout(pad=0)
    fig.savefig('build/figures/languages.pdf')


def interests(answers):
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

    fig, ax = plt.subplots(1, 1, figsize=(5.5, 3.3))

    interest.plot.barh(ax=ax)

    fig.tight_layout()
    fig.savefig('build/figures/interest.pdf')


if __name__ == '__main__':
    answers = pd.read_csv('data/2019.csv')
    languages(answers)
    operating_system(answers)
    programming(answers)
    interests(answers)
