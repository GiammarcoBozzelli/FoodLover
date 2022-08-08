
import argparse
import pandas as pd
import numpy as np
from csv import DictWriter

def has_numbers(input_string):
    """Return False if the string contains only letters"""
    return any(char.isdigit() for char in input_string)

def try_parse_int(num):
    """Try to parse a string in an intger; return True if parsing works"""
    try:
        int(num)
        return True
    except ValueError:
        return False


def try_parse_float(num):
    """Try to parse a string in a float; return True if parsing works"""
    try:
        float(num)
        return True
    except ValueError:
        return False


def name_input():
    """Control user input for food name"""
    stop = False

    if not has_numbers(user_in := input("Type food name: ")):
        # name contains only letters
        return user_in
    else:
        # name contains illegal characters
        print("\n", "You are allowed only to use letters for name, TRY AGAIN!", "\n")
        while not stop:
            # loop for input only correct characters
            if not has_numbers(user_in := input("Type food name: ")):
                stop = True
            else:
                print("\n", "You are allowed only to use letters for name, TRY AGAIN!", "\n")

        return user_in


def number_input(property, is_float):
    """Control user input for food properties (i.e. fat, calories, carbs, ...)"""
    stop = False

    if is_float:
        # property is a float number
        if try_parse_float(user_in := input(f"Type food {property}: ")):
            # property is a float number
            return user_in
        else:
            # property contains illegal character(s)
            print("\n", f"You are allowed only to use floats for {property}, TRY AGAIN!", "\n")
            while not stop:
                # loop for input only correct digits
                if try_parse_float(user_in := input(f"Type food {property}: ")):
                    stop = True
                else:
                    print("\n", f"You are allowed only to use floats for {property}, TRY AGAIN!", "\n")

            return user_in

    else:
        # property is an intger number
        if try_parse_int(user_in := input(f"Type food {property}: ")):
            # property is an integer number
            return user_in
        else:
            # property contains illegal character(s)
            print("\n", f"You are allowed only to use integers for {property}, TRY AGAIN!", "\n")
            while not stop:
                # loop for input only correct digits
                if try_parse_int(user_in := input(f"Type food {property}: "), is_float):
                    stop = True
                else:
                    print("\n", f"You are allowed only to use integers for {property}, TRY AGAIN!", "\n")

            return user_in


def update_dataframe(df):
    """Collect user input using the functions above and then add it to the CSV file"""
    food_properties = dict()
    print("Welcome, here you can add a food to the database...")
    user_choice = input("WARNING! Quit is allowed only here, do you really want to continue? [[Y]/n] ").strip()

    if user_choice == "Y" or user_choice == "y" or user_choice == "":
        # user decides to modify CSV file
        food_properties["name"] = ["" + str(name_input()) + ""]
        food_properties["carbohydrate"] = [str(number_input("carbs", is_float = True)) + "g"]
        food_properties["total_fat"] = [str(number_input("fats", is_float = True)) + "g"]
        food_properties["protein"] = [str(number_input("proteins", is_float = True)) + " g"]
        food_properties["calories"] = [int(number_input("calories", is_float = False))]
        # collect all necessary dat
        df_from_dict = pd.DataFrame.from_dict(food_properties)
        df = pd.concat([df, df_from_dict], ignore_index=True)
        df.index = range(0, len(df["name"]))
        df = df[df.columns.drop(list(df.filter(regex="Unnamed")))]
        df.to_csv("nutrition.csv")
        # add row to dataframe and export it in CSV file
        print("File modified successfully")
    elif user_choice == "N" or user_choice == "n":
        # user decides NOT to modify CSV file
        print("Successfully exit adding process...")


def read_dataframe(file_name):
    df = pd.read_csv(file_name)

    df["name"] = df["name"].astype(str)
    df["name"] = df["name"].str.lower()
    df["name"] = df["name"].str.replace(",", "")

    return df.copy()

def get_info(arguments):
    df = read_dataframe('nutrition.csv')
    row = df.loc[df['name'] == arguments.food]  # ottengo la riga corrispondente al food specificato dall'utente
    output = ''
    if arguments.show == True:
        show_food(df)
        return None
    if arguments.add == True:
        update_dataframe(df)
        return None
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

    print(f"Name: {arguments.food}\n" + output)
    return None

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

def show_food(df):
    letter = input('Type the starting letters of the food you are looking for: \n')
    out = df[df['name'].str.startswith(letter)]     #tutti i cibi che iniziano con la lettera specificata dall'utente (letter)
    out = out.reset_index(drop=True)                  #reset degli indici delle righe, numerati  1, 2, ..., n
    print(out['name'])                              #return solamente della colonna name
    return