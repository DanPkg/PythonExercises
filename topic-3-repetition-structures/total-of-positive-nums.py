# Program to calculate the sum of a series of positive numbers

# Variable for the running total of positive numbers entered
total = 0

number = float(input('Enter a positive number (negative to exit) : '))

while number >= 0:   
    
    total += number    
    number = float(input('Enter next positive number (negative to exit) : '))

print("Total of positive numbers is:", total)
