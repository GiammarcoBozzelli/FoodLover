def check_input(args):
    '''Checks that the input food is made of only alphanumeric characters'''
    if not args.food.isalpha():
        print('There is something wrong with your food name... Try with'
              + ' something like \'Apple\'')
        return(False)

    return True
