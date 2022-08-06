from csv import DictWriter
import pandas as pd


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def try_parse_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def try_parse_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def name_input():
    stop = False
    
    if not has_numbers(user_in := input("Type food name: ")):
        return user_in
    else:
        print("\n", "You are allowed only to use letters for name, TRY AGAIN!", "\n")
        while not stop:
            if not has_numbers(user_in := input("Type food name: ")):
                stop = True
            else:
                print("\n", "You are allowed only to use letters for name, TRY AGAIN!", "\n")
        
        return user_in


def number_input(property, is_float):
    stop = False
    
    if is_float:
        if try_parse_float(user_in := input(f"Type food {property}: ")):
            return user_in
        else:
            print("\n", f"You are allowed only to use floats for {property}, TRY AGAIN!", "\n")
            while not stop:
                if try_parse_float(user_in := input(f"Type food {property}: ")):
                    stop = True
                else:
                    print("\n", f"You are allowed only to use floats for {property}, TRY AGAIN!", "\n")
            
            return user_in

    else:
        if try_parse_int(user_in := input(f"Type food {property}: ")):
            return user_in
        else:
            print("\n", f"You are allowed only to use integers for {property}, TRY AGAIN!", "\n")
            while not stop:
                if try_parse_int(user_in := input(f"Type food {property}: "), is_float):
                    stop = True
                else:
                    print("\n", f"You are allowed only to use integers for {property}, TRY AGAIN!", "\n")
            
            return user_in


def update_dataframe(df):
    food_properties = dict()
    input("Welcome, here you can add a food to the database...")
    user_choice = input("WARNING! Quit is allowed only here, do you really want to continue? [Y/n] ")
    if user_choice == "Y" or user_choice == "y":
        food_properties["name"] = ["" + str(name_input()) + ""]
        food_properties["carbohydrate"] = [str(number_input("carbs", is_float = True)) + "g"]
        food_properties["total_fat"] = [str(number_input("fats", is_float = True)) + "g"]
        food_properties["protein"] = [str(number_input("proteins", is_float = True)) + " g"]
        food_properties["calories"] = [int(number_input("calories", is_float = False))]

        df_from_dict = pd.DataFrame.from_dict(food_properties)
        df = pd.concat([df, df_from_dict], ignore_index=True)
        df.index = range(0, len(df["name"]))
        df = df[df.columns.drop(list(df.filter(regex="Unnamed")))]
        df.to_csv("nutrition.csv")

        print("File modified successfully")

    else:
        print("Successfully exit adding process...")
