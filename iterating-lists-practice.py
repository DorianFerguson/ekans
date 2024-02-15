rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Idigo', 'Violet']
#            0.       1.        2.       3.       4.      5.        6

for color in rainbow: # can define any control varibale, I chose color
    print('Current color:', color)
    # list prints in order, but does not provide index
    
for color_index in range(len(rainbow)):
    print('Current index:', color_index, '| Current color:', rainbow[color_index])
    # with strings, len returns the number of characters
    # with lists, len returns the number of elements
    # range(len(rainbow)), means the range of 7, or rainbow[:7], so the loop will
    # will go through all its elements, 0-6




spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
low_spendings = 0
normal_spendings = 0
high_spendings = 0

for spent in spendings:
    if spent < 1000.0:
        low_spendings += 1
    elif spent >= 1000.0 and spent <= 2500.0:
        normal_spendings += 1
    else:
        high_spendings += 1

print('Numbers of months with low spendings:', str(low_spendings) + ',' ,'normal spendings:', str(normal_spendings) + ',', 'high spendings:', str(high_spendings) + '.' )