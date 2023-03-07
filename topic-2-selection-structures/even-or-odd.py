user_number = int(input('Enter an integer number: '))

if user_number > 0:
    print('Positive')
elif user_number < 0:
    print('Negative')
else:
    print('Zero')
    
# Use remainder operator % to determine perfectly divisible by 2
if (user_number % 2) == 0: 
    print ("Even") 
else: 
    print ("Odd")
