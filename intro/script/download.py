from getpass import getpass
import json
import requests
import pandas as pd

r = requests.get(
    "https://registration.pep-dortmund.org/events/16/participants",
    headers={"accept": "application/json"},
    auth=(input("Username: "), getpass()),
)
# make sure request was successfull
r.raise_for_status()

data = r.json()
remarks = []
other_interests = []


def get_data(p):
    data = p["data"].copy()
    del data["name"]
    del data["email"]
    if data["remarks"] != "":
        remarks.append(data["remarks"])
    if data["other_interesets"] != "":
        other_interests.append(data["other_interesets"])
    del data["remarks"]
    del data["other_interesets"]

    return data

part_status = []
for p in data["participants"]:
    if p["status_name"] == "confirmed":
        part_status.append(p)


participants = [get_data(p) for p in part_status]

with open("data/toolbox2023.json", "w") as f:
    json.dump(participants, f, indent=2)


keys = ["os", "installieren", "toolbox", "latex"]
df = pd.DataFrame([{k: p[k] for k in keys} for p in participants])

for part in ("installieren", "toolbox", "latex"):
    print("\n")
    print(part, "\t\t", df[df[part]]["os"].value_counts().sum())
    print(df[df[part]]["os"].value_counts())

print("Anmerkungen:", *remarks, sep="\n\t")
print("\nWeitere Interessen:", *other_interests, sep="\n\t")
