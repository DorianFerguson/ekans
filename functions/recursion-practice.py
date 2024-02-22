# factorial: the product of an integer and all the integers below it
# 3! = 1 * 2 * 3 = 6
# 5! = 1 * 2 * 3 * 4 * 5 = 120
def get_factorial (number):
    factorial = 1
    for x in range(1, number + 1 ):
        factorial *= x
    return factorial

print(get_factorial(6))

# the factorial of a given interger is always the product of the factorial
# of the previous interger and the given interger itself

# For example, the following:
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# 5! = 1 * 2 * 3 * 4 * 5

# can be re-written as:
# 1! = 1
# 2! = 2 * 1!
# 3! = 3 * 2!
# 4! = 4 * 3!
# 5! = 5 * 4!

def get_factorial_recursive(number):
    if number <= 1: # recursive funtions need a stop condition
        return 1
    return number * get_factorial_recursive(number - 1) # the funtion calling itself is a major point of recursion

print(get_factorial_recursive(6))