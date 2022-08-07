import argparse


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
