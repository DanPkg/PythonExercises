'''
Write a program that should ask the user to enter a positive integer n. 
Based on the value of n, the program should use a nested loop to draw 
the following pattern with n rows:
*
**
***
****
*****
'''

# Get the positive integer from user.
n = int(input('Enter a positive integer: '))

for i in range(1, n+1):
    print('*' * i)



    
# Another option as requested to use nested loop:
n = int(input('Enter a positive integer: '))
my_char = '*'
for i in range(1, n+1):
    
    for _ in range(i): # use underscore as iterator is not used in loop
        print(my_char, end='') # use end so it doesn't create new line yet
    
    print()
