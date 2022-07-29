import argparse
import pandas as pd
from input import parse_arguments
from check import check_input

if __name__ == '__main__':

    # Retrieve user input from terminal
    arguments = parse_arguments()
    if check_input(arguments):
        print(arguments)
    else:
        quit  # Check if the input is a valid food in the dataset (Chiara)
