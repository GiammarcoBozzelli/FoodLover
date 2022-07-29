
def check_input(args):
    '''Checks that the input food is made of only accepted characters'''
    if args.food.isalpha():
        return True
    else:
        print('There is something wrong with your food name... Try with'
              + ' something like \'Apple\'')
        return False
