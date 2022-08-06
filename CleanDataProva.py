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

def get_info(arguments):
    df = read_dataframe('nutrition.csv')
    row = df.loc[df['name'] == arguments.food] # ottengo la riga corrispondente al food specificato dall'utente
    output = f"Name: {arguments.food}\n"
    # TODO: rimuovere pass una volta scritto il codice all'interno del blocco IF
    if arguments.show == True:
        pass
    if arguments.add == True:
        update_dataframe(df)
    if arguments.protein == True:
        output += "protein: " + str(row["protein"].values[0]) + "\n"
    if arguments.calories == True:
        output += "calories: " + str(row["calories"].values[0]) + ' kcal' + "\n"
    if arguments.carbs == True:
        output += "carbs: " + str(row["carbohydrate"].values[0]) + "\n"
    if arguments.fats == True:
        output += "fats: " + str(row["total_fat"].values[0]) + "\n"
    if not arguments.add and not arguments.protein and not arguments.carbs and not arguments.fats and not arguments.calories and not arguments.show:
        output += "protein: " + str(row["protein"].values[0]) + "\n"
        output += "calories: " + str(row["calories"].values[0]) + ' kcal' + "\n"
        output += "carbs: " + str(row["carbohydrate"].values[0]) + "\n"
        output += "fats: " + str(row["total_fat"].values[0]) + "\n"

    return output


