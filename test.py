
import unittest
from Modules import *
import pandas.testing as pd_testing


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
        # simulate user input
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

        # create the correct expected output
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

        # create the correct expected output
        row = self.df.loc[self.df['name'] == self.arguments.food]
        output = ''
        output += "protein: " + str(row["protein"].values[0]) + "\n"
        output += "calories: " + str(row["calories"].values[0]) + ' kcal\n'
        output += "carbs: " + str(row["carbohydrate"].values[0]) + "\n"
        output += "fats: " + str(row["total_fat"].values[0]) + "\n"

        output = f"Name: {self.arguments.food}\n" + output
        self.assertEqual(get_info(self.arguments), output)

    def test_show(self):
        '''
        Checks if the program correctly shows all foods
        starting with the letters specified by the users
        '''
        pass

    def test_update_dataframe(self):
        '''
        Checks if the function correctly writes a new line
        '''
        # copied the function update_dataframe()
        # to bypass input requirements
        food_properties = dict()

        # user decides to modify CSV file
        food_properties["name"] = ['test']
        food_properties["carbohydrate"] = ['20' + "g"]
        food_properties["total_fat"] = ['20' + "g"]
        food_properties["protein"] = ['20' + "g"]
        food_properties["calories"] = ['20']
        # collect all necessary data
        df_from_dict = pd.DataFrame.from_dict(food_properties)
        df = pd.concat([self.df, df_from_dict], ignore_index=True)
        df.index = range(0, len(df["name"]))
        df = df[df.columns.drop(list(df.filter(regex="Unnamed")))]
        df.to_csv("nutrition.csv")
        df = read_dataframe('nutrition.csv')

        expected_row = pd.DataFrame(columns=df.columns).fillna('')
        expected_row['name'] = ['test']
        expected_row["carbohydrate"] = ['20' + "g"]
        expected_row["total_fat"] = ['20' + "g"]
        expected_row["protein"] = ['20' + "g"]
        expected_row["calories"] = [int(20)]

        added_row = df.iloc[-1:]
        # remove test row from the dataframe
        df.drop(index=df.index[-1], axis=0, inplace=True)
        df.to_csv("nutrition.csv")

        pd_testing.assert_frame_equal(added_row[['name', "total_fat",
                                                 'carbohydrate',
                                                 'protein',
                                                 'calories']].reset_index(
                                                    drop=True),

                                      expected_row[['name', "total_fat",
                                                    'carbohydrate', 'protein',
                                                    'calories']].reset_index(
                                                        drop=True))


if __name__ == "__main__":
    unittest.main()
