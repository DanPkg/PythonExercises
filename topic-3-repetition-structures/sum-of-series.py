''' 
Write a program to calculate the sum of the following series
The program should prompt the user for a positive integer n and display
the sum of the series. S = 1 + 1/2 + 1/4 + 1/8 +...+ 1/2**n
'''
total_sum = 0

n = int(input('Enter a positive integer: '))

# Loop n + 1 times
for x in range(n+1):
    formula = 1 / (2**x)    
    total_sum += formula
    
print('Sum of the series is ', total_sum)



# Course coordinator's code:
# Get the value of n
n = int(input('Enter the value of n: '))
total = 0.0

# Loop n+1 times (0 to n)
for i in range(n+1):
    total += 2 ** -i # Calculate the value for the i-th term and accumulate it

# Display the sum
print('The sum of the series is ', total)
