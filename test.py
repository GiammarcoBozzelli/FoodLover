
import unittest
from Modules import *


class TestInputsValues(unittest.TestCase):

    arguments = parse_arguments()
    df = read_dataframe('nutrition.csv')

    def test_valid_name(self):
        '''
        The function test if passed a food present in the
        progam is able to detect the input as valid
        '''
        # simulate valid user input
        self.arguments.food = ['Cornstarch']
        self.assertTrue(check_input(self.arguments))

    def test_empty_input(self):
        '''
        Check if given empty input the progam returns False
        '''
        # simulate empty input
        with suppress_stdout():
            out = check_input(self.arguments)
        self.assertFalse(out)

    def test_empty_input_argument(self):
        '''
        Check if given empty input and invalid argument
        the progam returns False
        '''
        # simulate user input
        self.arguments.protein = True
        with suppress_stdout():
            out = check_input(self.arguments)
        self.assertFalse(out)

    def test_invalid_input(self):
        '''
        The function test if passed a food present in the
        progam is able to detect the input as valid
        '''
        #simulate user input
        self.arguments.food = ['ciao!32']
        with suppress_stdout():
            out = check_input(self.arguments)
        self.assertFalse(out)

    def test_get_info(self):
        '''
        Test if all arguments work when passed as arguments
        '''
        # simulate user input
        self.arguments.food = 'cornstarch'
        self.arguments.calories = True
        self.arguments.protein = True
        self.arguments.fats = True
        self.arguments.carbs = True

        row = self.df.loc[self.df['name'] == self.arguments.food]
        output = ''
        output += "protein: " + str(row["protein"].values[0]) + "\n"
        output += "calories: " + str(row["calories"].values[0]) + ' kcal\n'
        output += "carbs: " + str(row["carbohydrate"].values[0]) + "\n"
        output += "fats: " + str(row["total_fat"].values[0]) + "\n"

        output = f"Name: {self.arguments.food}\n" + output
        self.assertEqual(get_info(self.arguments), output)

    def test_get_info_no_arguments(self):
        '''
        Test if all arguments work when passed as arguments
        '''
        # simulate user input
        self.arguments.food = 'cornstarch'

        row = self.df.loc[self.df['name'] == self.arguments.food]
        output = ''
        output += "protein: " + str(row["protein"].values[0]) + "\n"
        output += "calories: " + str(row["calories"].values[0]) + ' kcal\n'
        output += "carbs: " + str(row["carbohydrate"].values[0]) + "\n"
        output += "fats: " + str(row["total_fat"].values[0]) + "\n"

        output = f"Name: {self.arguments.food}\n" + output
        self.assertEqual(get_info(self.arguments), output)

    def test_add(self):
        pass

    def test_show(self):
        pass


if __name__ == "__main__":
    unittest.main()
