# collections used to store key value pairs

emails = {
    'Anne Stahl': 'astahl@example.com',
    'Draco Mann': 'bigdrac0@example.com',
    'Hugh Jackman': 'claws89@example.com'
}
print(emails['Hugh Jackman'])

# Keys must be unique, othewise one gets replaced
# Can only be used by 'searching' by key
# Key must be immutable
# Value can be any data type

grades = {}
grades ['John'] = 'A-'
grades ['Anne'] = 'B+'
#print(grades)
#grades ['Anne'] = 'A-'
#print(grades)
#grades.update({'John':'A+'})
#print(grades)

#print(len(grades))

#if 'John' in grades:
#    print('John got an', grades['John'])

#del grades['John']
#print(grades)

#===== ITERATION =======
#for x in grades:
#    print(x) # returns keys
    
#for x in grades.keys():
#    print(x) # returns keys

#for x in grades.values():
#    print(x) # returns values

#for person, grade in grades.items():
#   print(person, 'got', grade) # returns both key and values

sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    request = input('Enter a word in English or EXIT: ')
    if request == 'EXIT':
        break
    if request in sample_dict:
        print('Translation:',sample_dict[request])
    else:
        print('No match!')
print('Bye!')

#print sample_dict.items() #retruns tuples with the key value pairs
# for k, v in sample_dict.tems()
#    print (k, v) # prints the key value pairs in vertical list
#    for i in value:
#        print(i)