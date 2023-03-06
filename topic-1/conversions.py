KGS_PER_POUND = 0.454

# Convert and display kilograms to pounds from user input
pds = float(input('Enter the mass of the object in pounds: '))
kgs = pds * KGS_PER_POUND
print(f"{kgs} kilograms")
print(pds, 'is equivalent to', format(kgs, '.2f'), 'kilograms')

# Convert and display celsius to fahrenheit to from user input
temp_celsius = float(input('Enter the temperature in Celsius units: '))
conv_to_fahren = (9/5) * temp_celsius + 32
print(f"{conv_to_fahren:.2f} Fahrenheit")
print(format(conv_to_fahren, '.2f'), 'Fahrenheit')
