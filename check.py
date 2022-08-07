

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
