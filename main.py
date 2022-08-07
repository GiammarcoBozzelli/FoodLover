import argparse
import pandas as pd
from input import parse_arguments
from check import check_input


if __name__ == '__main__':

    # Retrieve user input from terminal
    # and controls if the input is valid
    arguments = parse_arguments()
    if check_input(arguments):  # check if the food is in the dataset
        arguments.food = ' '.join(arguments.food).lower()
        get_info(arguments)  # outputs the required infos
