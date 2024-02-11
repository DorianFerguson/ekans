#counter = 1
#while counter < 11:
#    print(counter)
#    counter += 1
#print('Finished!')

#secret_number = 8
#print('''=======================
#=== SECRET NUMBER GAME===
#=======================''') # Use three single quotes to print muli-line strings
#user_guess = int(input('Try to guess the secret number from 0 to 20: '))
#while user_guess != secret_number:
#    print('Wrong!')
#    user_guess = int(input('Try to guess the secret number from 0 to 20: '))
#print("Correct! That\'s the secret number!")

#for character in 'Hello, world!':
#    print('Current chracater:', ch)

#for counter in range(1,11): #range (start,stop, icrease)
#    print(counter)
#    print('Finished!')

#while True:
#    name = input('Enter your name or \'EXIT\' to close the program: ')
#    if (name == 'EXIT'):
#        break # used to exit loop
#    print('Hello', name)
    
#for i in range(1,21):
#    if i % 5 == 0:
#        continue #used to move to next iteration
#    print(i)

# use pass instruction as a place holder. loops need a body to work

while True:
    user_guess = int(input('When was Python 1.0 released? '))
    if (user_guess > 1994):
        print('It was earlier than that!')
    elif (user_guess < 1994):
        print('It was later than that!')
    else:
        print('Correct!')
        break