rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Idigo', 'Violet']
#            0.       1.        2.       3.       4.      5.        6

print(rainbow)

print(rainbow[1]) #indexing, notice this returns a string value
print(rainbow[-5])

print(rainbow[0:2]) #slicing first index is start, second is the end point
# first index is inlcusive, second is exclusive. a list is a result
print(rainbow[:2]) # leaving an index blanck means to start or end from the
# beginning or end of the list. This example starts from the beginning
# inclusive, and ends at 2, exclusive.

print(rainbow[2:]) #this starts at 2, inclusive, and ends at the end of
# the list.

print(rainbow[:]) # this means all elements

del rainbow[1] #deletion by indexing.

print(rainbow)

del rainbow[3:] #deletes by splicing

print(rainbow)

del rainbow[:] # deletes all elements

print(rainbow)

#del rainbow # will delete the list itself

#print(rainbow) # will cause an error as the list is deleted

# Use the .append method to add data to the end of a list

rainbow.append('Red') #takes one argument
print(rainbow)

#Use the .insert method to add items anywhere in the list
rainbow = ['Red', 'Orange', 'Yellow', 'Blue']
print(rainbow)
rainbow.insert(3,'Green') # assumes specified index, pushes everything right
print(rainbow)