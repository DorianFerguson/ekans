import random
def name_generator(par1, par2):
    while True:
        qty = int(par1)
        dept = str(par2)
        dept.lower() == 'marketing' or 'finops' or 'accounting'
        characters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890-!'
        name_length = 8
        if dept.lower() == 'marketing':
            for names in range(0,qty):
                generated_name = 'mar' + "".join(random.choices(characters,k = name_length))
                print(generated_name)
        elif dept.lower() == 'finops':
            for names in range(0,qty):
                generated_name = 'fin' + "".join(random.choices(characters,k = name_length))
                print(generated_name)
        elif dept.lower() == 'accounting':
            for names in range(0,qty):
                generated_name = 'acc' + "".join(random.choices(characters,k = name_length))
                print(generated_name)
        else:
            print('Your department does not have access to this generator.')
            break
        break


name_generator(5, 'MarkEting')