import pandas as pd
import openpyxl
import unidecode

df = pd.read_excel("input/Membres promo 21 avril 2021.xlsx", header=8, usecols="B:F")
participants = pd.DataFrame(columns=["email", "lastname", "firstname"], index=df.index)
participants["lastname"] = df["nom_choisi"]
participants["firstname"] = df["prenom_choisi"]
participants["email"] = df["co_id_pers"]+"@usherbrooke.ca"
# for i, row in participants.iterrows():
#     participants.iloc[i, 0] = unidecode.unidecode(f"{participants.iloc[i, 2]}.{participants.iloc[i, 1]}@usherbrooke.ca")

participants.to_csv("output/participants.csv",index=False)

