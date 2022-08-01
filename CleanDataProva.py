import pandas as pd
import numpy as np


def read_dataframe(file_name):
    df = pd.read_csv(file_name)

    df["name"] = df["name"].astype(str)
    df["name"] = df["name"].str.lower()
    df["name"] = df["name"].str.replace(",", "")

    return df.copy()


def read_dataframe(file_name):
    df = pd.read_csv(file_name)

    return df.copy()

def get_info(df, food, verbose, show, add, protein, calories, carbs, fats):
    row = df.loc[df['name'] == food] #ottengo la riga corrispondente al food specificato dall'utente
    output = ""
    # TODO: rimuovere pass una volta scritto il codice all'interno del blocco IF
    if verbose == True:
        pass
    if show == True:
        pass
    if add == True:
        pass
    if protein == True:
        output += "protein: " + str(row["protein"].values[0]) + "\n"
    if calories == True:
        output += "calories: " + str(row["calories"].values[0]) + "\n"
    if carbs == True:
        output += "carbs: " + str(row["carbohydrate"].values[0]) + "\n"
    if fats == True:
        output += "fats: " + str(row["total_fat"].values[0]) + "\n"
    return output



