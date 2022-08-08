import unittest
from Modules import *

class TestInputsValues(unittest.TestCase):
    
    arguments = parse_arguments()

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

if __name__ == "__main__":
    unittest.main()

