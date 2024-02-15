#empty_tuple = () #empty tuple needs parenthesis
#one_element_tuple_a = (1,)
#one_element_tuple_b = 1, # single elemnet tuple needs trailing comma
#three_element_tuple = 1, 2, 3 # needs neither parenthesis nor trailing comma

# Mutable data can be updated whenever
# Immutable data stays that way permanently
# tuples are immutable

#three_element_tuple.append(4) # error
#del three_element_tuple[0] # error
#sthree_element_tuple[0] = -1 #error
#print(three_element_tuple[0]) #sucess

# the same viewing and iteration operations as lists work with tuples

#user_data = ('Mike', 'Italian', 1964)
#print(user_data)

#user_data = ('Mike', 'Italian', 1964) + ('Plubmer', 'Male') # creats new tuple with items
#print(user_data)

# use lists when you have many values of the same data type
# use when values represent the same phenomena

# use tuples when grouping elements of differnt data types that 
# are somehow related, forming a greater 
# Tuples can use variables as well as literal
# areguments can be on either side of = sign, list swapping is actaully
# using tuples

#====== TUPLE LISTS ======

#city_1 = ('London', 'UK', 8.98)
#city_2 = ('canberra', 'Austrailia', 0.4)
#city_3 = ('Algiers', 'Algeria', 3.9)
#capitals = [('London', 'UK', 8.98), ('canberra', 'Austrailia', 0.4), ('Algiers', 'Algeria', 3.9) ]
#for capital in capitals:
#    print('Name:', capital[0], ', Contry:', capital[1], ', Population:', capital[2])
    
#user_data = ('Mike', 'Italian', 1964, [77.0, 78.5, 75.9])
#Last element of tuple is a list, which is mutable. the tuple cannot be changed
# but the list can

#user_data[3].append(76.8)
#print(user_data)



connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
to_rome = 0
time = 0
for flight in connections:
    if "Rome" in flight[1]:
        to_rome += 1
        time += flight[2]

print( to_rome, "connections lead to Rome with an\
average flight time of", time / to_rome, 'minutes.')