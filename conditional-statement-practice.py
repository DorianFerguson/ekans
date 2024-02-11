#age = int(input('What is your age? '))
#if age > 21:
#    print('You\'ve lived at least 21 years.')
#    print('You can buy alcoholic beverages in the U.S.A.!')
#elif age == 21: # Cann have multiple elifs, or none'
#    print('You\'ve truned 21 this year. Happy birthday!')
#    print('You can buy alcoholic beverages in the U.S.A.!')
#else:
#    print('You\'ve lived less than 21 years.')
#    print('No alcoholic beverages for you!')
    
    
#password = input('What is the password? ')
#if password != 'frankLuc@s':
#    print('Incorrect.')
#else:
#    print('Correct.')

#age = int(input('What is your age? '))
#country = input('What is your country? ')

#if not country == 'Germany' and age < 25 or \
#   country == 'Germany' and age < 23:
#       print('You qualify!')
#else:
#    print('You don\'t qualify.')

# order of operations is:
# 1. not
# 2. and
# 3. or

# Add brackets to inprove readability
#age = int(input('What is your age? '))
#country = input('What is your country? ')

#if ((not country == 'Germany') and age < 25) or \
#   (country == 'Germany' and age < 23):
#       print('You qualify!')
#else:
#    print('You don\'t qualify.')

# Nested IF statement

#answer_a = input('Do you like to travle? y/n: ')
#if answer_a == 'y':
#    answer_b = input('Would you like to travel to Asia? y/n:  ')
#    if answer_b == 'y':
#        print('Great! You could win a ticket Thailand')
#    elif answer_b == 'n':
#        print('Sorry to hear that.')
#    else:
#        print('Only \'y\' or \'n\' input allowed.')
#elif answer_a == 'n':
#    print('Sorry to hear that')
#else:
#    print('Only \'y\' or \'n\' input allowed.')
    

purchase_date = int(input('How many days ago have you purchased the item? '))
item_use = input('Have you used the item at all [y/n]? ')
item_defect = input('Has the item broken down on its own [y/n]? ')

if ((purchase_date <= 10 and item_use == 'n') or item_defect == 'y'):
    print('You can get a refund.')
else:
    print ('You cannot get a refund.')