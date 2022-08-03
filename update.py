from csv import DictWriter


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def has_only_numbers(input_string):
    return all(char.isdigit() for char in input_string)


def update_dataframe(df):
    # print(df.columns)
    # carbohydrate, total_fat, calories, name, protein
    f_name = input("Type food name: ")
    f_cal = input("Type food calories: ")
    f_carb = input("Type food carbs: ")
    f_fat = input("Type food fats: ")
    f_prot = input("Type food proteins: ")
    d = {"name": f_name, "carbohydrate": f_carb, "total_fat": f_fat, "protein": f_prot, "calories": f_cal}

    if not has_numbers(f_name):
        if has_only_numbers(f_cal) and has_only_numbers(f_carb) and has_only_numbers(f_fat) and has_only_numbers(f_prot):
            for k in df.columns:
                if k not in d:
                    d[k] = None

            with open("nutrition.csv", "a") as fp:
                dictwriter_object = DictWriter(fp, fieldnames=d)

                dictwriter_object.writerow(d)

                fp.close()
            print("File modified successfully")
        else:
            print("Wrong input, please try again")
    else:
        print("Wrong input, please try again")
