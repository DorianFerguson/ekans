# Variable Practice
greeting = 'Hello, friend'
print(greeting)

# Intergers are whole numbers
age = 29

# Floats are decinaml numbers. Sometimes noted with comas
speed = 7.3
speed2 = 8,5

# Booleans are True or False values. False = 0 True = 1
will_i_succeed_ = True

# Use underscores in numbers to improve readability
12_000_300

# octal numbers start with 0o or 0o. Digits can only range 0-7
print(0o123)

# Hexadecimal numbers start with 0X or 0x
print(0x123)

# Use the ' + ' operator for addition
2 + 3

# Use the ' - ' operator for subtraction

8 - 4

# Use the ' * ' operator for multiplication

2 * 9

6 / 2 # standard division, '/' returns a float
7 // 2 # integer division, '//' returns the nearest whole number, round down
6 % 2 # modulus division, '%' retruns the remainder

# Use the power operator, '**' for exponets
2 ** 3 # 2^3

# For operators that reurn intergers, they will always return flots IF feed one

income = 250_000
lowtaxland_rate = income * 0.05
ripoffland_rate = income * 0.43
lowtax_calculation = income * lowtaxland_rate
hightax_calculation = income * ripoffland_rate
difference = hightax_calculation - lowtax_calculation
print('Your income is',income, 'you would pay', lowtax_calculation, 
'income tax in Lowtaxland or', hightax_calculation, 
'in Ripoffland. You would save' ,difference, 
'by paying taxes in Lowtaxland!')

# reasign varibales by sating it's equal to another value
age = 21
age = 23
age += 7 # this is a qucik way to add to the current value
age *= 7 # this is a qucik way to multiply the current value
age -= 7 # this is a qucik way to subtract from the current value
age /= 7 # this is a qucik way to divide the current value

# Use '+' to concatenate strings
string = "hello" + "world" 
print(string) # note the output does note have any spaces

print(string * 5)

username = input('What is your name? ') # this will be treated as a string
print('Hello,',username)

login = input('Enter your login: ')
lang = input('Enter your native language: ')
print('Your login is', login ,'and you speak', lang)
