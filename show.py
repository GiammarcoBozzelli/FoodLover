import pandas as pd


def show_foods():
    '''
    Prints the whole list of available foods
    '''
    df = pd.read_csv('pathtocsv')
    for x in df.rows:
        print(df.rows['name'], '\n')
    return
