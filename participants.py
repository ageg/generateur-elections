import pandas as pd
import unidecode

df = pd.read_excel("input/H21 - Liste complète.xlsx", header=8, usecols="B:F")
df2 = pd.read_excel("input/AGEGListeComplèteA20.xlsx", header=8, usecols="B:F")
participants = pd.DataFrame(columns=["email", "lastname", "firstname"], index=df.index)
participants["lastname"] = df["Nom choisi"]
participants["firstname"] = df["prénom choisi"]
for i, row in participants.iterrows():
    participants.iloc[i, 0] = unidecode.unidecode(f"{participants.iloc[i, 2]}.{participants.iloc[i, 1]}@usherbrooke.ca")

participants.to_csv("output/participants.csv",index=False)
