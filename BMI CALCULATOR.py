name = input('Enter your name: ')
print('~~~~~~~~~~~~~~~~~~~~~~')
weight = int(input('Enter your Weight in Pound: '))
print('~~~~~~~~~~~~~~~~~~~~~~')
height = int(input('Enter your Height in inches: '))
print('~~~~~~~~~~~~~~~~~~~~~~')

BMI = (weight * 703)/(height * height)
print(name + ' your BMI is ' + str(BMI))