
import argparse
from matplotlib.pyplot import show
import pandas as pd
import numpy as np
from csv import DictWriter


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

def parse_arguments():
    '''Parse command arguments'''
    parser = argparse.ArgumentParser(description='Retrieve food name'
                                     + 'input from the users')
    parser.add_argument('food', action='store', nargs='*', help='Input the '
                        + 'name of the food you would like to know more about',
                        type=str)
    parser.add_argument('-s', '--show', action='store_true', help='Add -s to '
                        + 'your input to show all foods in the database')
    parser.add_argument('-a', '--add', action='store_true', help='Add a food '
                        + 'to the database')
    parser.add_argument('-p', '--protein', action='store_true', help='Displays'
                        + ' how many grams of proteins the food has per 100g')
    parser.add_argument('-cal', '--calories', action='store_true', help=''
                        + 'Displays how many calories the food has per 100g')
    parser.add_argument('-f', '--fats', action='store_true', help='Displays '
                        + 'how many grams of fats the food has per 100 grams')
    parser.add_argument('-c', '--carbs', action='store_true', help='Displays '
                        + 'how many grams of carbohydrates the food has '
                        + 'per 100g')

    return parser.parse_args()


def check_input(args):
    '''Checks that the input food is made of only accepted characters
       and if it is present in the database if not, it returns an
       error message to the user'''
    food_name = ' '.join(args.food).lower()
    df = read_dataframe('nutrition.csv')
    
    if args.show:
        show_food(df)
        quit()
    elif args.food == []:
        print('Type the food you are interested in after \"main.py\"')
        quit()

    if all(x.isalpha() or x.isspace() for x in food_name):
        if args.add:
            if food_name in df.values:
                print('This food is already in the database! \nType '
                      + 'again the command without -a to get information'
                      + f' about \"{food_name}\"')
                return False
            else:
                return True
        else:
            if food_name in df.values:
                return True
            else:
                print('We are sorry but this food is not in our database :('
                      + '\nYou can help us out and fill it yourself!\n'
                      + 'All you have to do is relaunching the progra'
                      + 'adding \"-a\" to your command!')
                return False
    else:
        print('There is something wrong with your food name... Try again '
              + 'with something like \'Apple\' and avoid using special'
              + ' characters or numbers!')
        return False

