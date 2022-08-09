from re import T
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
        self.arguments.food = ['Cornstarch']
        self.assertTrue(check_input(self.arguments))

    def test_empty_input(self):
        '''
        Check if given empty input the progam returns False
        '''
        self.assertFalse(check_input(self.arguments))

    def test_invalid_input(self):
        '''
        The function test if passed a food present in the
        progam is able to detect the input as valid
        '''
        self.arguments.food = ['!321354']
        self.assertFalse(check_input(self.arguments))
    
    def test_get_info(self):
        '''
        Test if all arguments work when passed as arguments
        '''
        self.arguments.food = 'cornstarch'
        self.arguments.calories = True
        self.arguments.protein = True
        self.arguments.fats = True
        self.arguments.carbs = True
        
        row = self.df.loc[self.df['name'] == self.arguments.food]
        output = ''
        output += "protein: " + str(row["protein"].values[0]) + "\n"
        output += "calories: " + str(row["calories"].values[0]) + ' kcal' + "\n"
        output += "carbs: " + str(row["carbohydrate"].values[0]) + "\n"
        output += "fats: " + str(row["total_fat"].values[0]) + "\n"

        output = f"Name: {self.arguments.food}\n" + output
        print(output)
        self.assertEqual(get_info(self.arguments),output)



if __name__ == "__main__":
    unittest.main()
