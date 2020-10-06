from getpass import getpass
import json
import requests
import pandas as pd

r = requests.get(
    'https://registration.pep-dortmund.org/events/4/participants',
    headers={'accept': 'application/json'},
    auth=(input('Username: '), getpass())
)
# make sure request was successfull
r.raise_for_status()

data = r.json()


def get_data(p):
    data = p['data'].copy()
    del data['name']
    del data['email']

    return data

participants = [get_data(p) for p in data['participants']]

with open('data/toolbox2020.json', 'w') as f:
    json.dump(participants, f, indent=2)

list = []
for participant in participants:
    if (participant['installieren'] == True):
        list.append(participant['os'])
os = pd.Series(list).value_counts()
print("Installieren\t", os.sum())
print(os)

list = []
for participant in participants:
    if (participant['toolbox'] == True):
        list.append(participant['os'])
os = pd.Series(list).value_counts()
print("\nToolbox\t\t", os.sum())
print(os)

list = []
for participant in participants:
    if (participant['latex'] == True):
        list.append(participant['os'])
os = pd.Series(list).value_counts()
print("\nLatex\t\t", os.sum())
print(os)
