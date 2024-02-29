try: # try statemnt must have at least one except
    value = int(input('What integer would you like to invert?'))
    print('The inverse of', value, 'is', 1/value)
except:
    print('Zero or letters are not valid!')
# this is an example of a universal except
# all errors will result in this branch

try: 
    value = int(input('What integer would you like to invert?'))
    print('The inverse of', value, 'is', 1/value)
except ValueError: # branch made for specified errors
    print('Only numbers are allowed!')
except ZeroDivisionError: 
    print('Division by 0 is impossible!')

#easiest way to find out possible errors is to intentionally 
# provide invalid input, then create a branch for it