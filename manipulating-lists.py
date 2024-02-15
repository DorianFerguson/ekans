#first = input('Enter first number: ')
#second = input('Enter second number: ')
#print('Before swap:', 'First is', first,'and second is', second)
#first, second = second, first
#print('After swap:', 'First is now',first,'and second is now', second)

#fav_ice_cream = ['Vanilla', 'Peanut butter', 'Cherry garcia', 'Lavender']
#fav_ice_cream[0], fav_ice_cream[3] = fav_ice_cream[3], fav_ice_cream[0]
#print(fav_ice_cream)

#fav_ice_cream.sort() # .sort method sorts elements in alpha-numeric order
#fav_ice_cream.sort(reverse=True) # sorts in reverse
# .sort is a method, so only for permanent use

#print(sorted(fav_ice_cream)) #use this function for temporary results, as it
#does not affect the original list
#print(fav_ice_cream)

# ======= PRESENCE IN LIST ===============
#available_sizes = ['small', 'medium', 'large']
#request = input('What size shirt do you want? ').lower()
#if request in available_sizes:
#    print('We have more available in that size!')
#else:
#    print('We\'re out of that size.')

#if request not in available_sizes:
#    print('We\'re out of that size.')
#else:
#    print('We have more available in that size!')
    
#===== COPYING LISTS =====
#og_list = [1, 2, 3, 4, 5,]
#new_list = og_list[:] # the slicing causes this to be a new list
# instead of a new reference to the same list
#og_list[0] = -3
#print('Original: ', og_list, '\nNew:', new_list)

#====== LIST COMPREHENSIONS ======
#Say I wanted to make a list 1-100

#numbers = []
#for x in range(1, 101):
#    numbers.append(x)
#print(numbers)

# That works, but python has built in comprehensions to make this simpler

#numbers = [x for x in range(1, 101)] # note variable x before the loop
#print(numbers)

# Much easier, such concise

#numbers = [x for x in range(1, 101) if x % 3 != 0] # bye numbers divisible by 3
#print(numbers)

#======== NESTED LISTS=========
#cells = [['A1','A2', 'A3'], ['B1', 'B2', 'B3']]
#print(cells[0]) # returns element in outer list, which the A block
#print(cells[0] [0]) # returns element from inner list which is cell A1

#for x in cells:
#    print('Element:', x) # returns elements of outer list

#for x in cells:
#    for y in x:
#        print('Element:', y) # use nested loops for nested elements

# Let's make this look like a table
#table = [['A1','A2', 'A3'], ['B1', 'B2', 'B3']]
#for row in table:
#    for cell in row:
#        print(cell, '', end='')
#    print()

#table = [[x for x in range(1,6)] for y in range(4)]
            #inner loop             #outer loop
# completes the inner loop comprehension until the outer loop comp, is complete

#======= LIST CAT =======
left_list = [1, 2, 3, 4]
right_list = [5, 6, 7, 8]
whole_list = left_list + right_list
print(whole_list)

use_list = [8, 8] * 8
print(use_list)
