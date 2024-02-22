# generators: used to return multiple values one at a time
def get_number():
    for x in range(1,4):
        yield x

# generator must be stored in a variable
generator = get_number()

print(next(generator)) # use next to get next value
print(next(generator))
print(next(generator)) # generator always remembers the previuos vale, so the next funtion can get the next value.

# use a for loop to iterate over generator values
for x in get_number():
    print(x)

# turn generator values into list
numbers = list(get_number())
print(numbers)