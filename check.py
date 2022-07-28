import re


def check_input(args):
    '''Checks that the input food is made of only alphanumeric characters'''
    if re.search(args.food.lower(), ['a-z ,']):
        return True
    else:
        print('There is something wrong with your food name... Try with'
              + ' something like \'Apple\'')
        return False
