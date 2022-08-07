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
