# Find and display middle number out of 3 numbers

A = int(input('1. Enter a number: '))
B = int(input('2. Enter a number: '))
C = int(input('3. Enter a number: '))

middle_num = min(max(A,B), max(B,C), max(A,C))
print('Middle number is:', middle_num)


# Option 2
if (B < A < C) or (B > A > C):
    middle_num = A
elif (A < B < C) or (A > B > C):
    middle_num = B
else:
    middle_num = C
print('Middle number is:', middle_num)


# Option 3
middle_num = sorted([A, B, C])[1] # middle index of sorted list
print(middle_num)
