'''
At a university, the tuition fee for a full-time student is $8,000 per 
semester. It has been announced that the fee will increase by 2 percent each 
year for the next 5 years. Write a program with a loop that displays the 
projected semester tuition amount for the next 5 years.
'''

# Note: I misread the requirements, below is 2% increase per semester, 
#       and the display output is per semester fee.

semesters = 2 # two semesters in AU
years = 5

SEMESTER_ORIG_FEE = 8000.00
FEE_INCREASE = 0.02

current_fee = SEMESTER_ORIG_FEE

for year in range(1, years + 1):
    
    for semester in range(1, semesters + 1):
    
        current_fee += (current_fee * fee_increase)
        print('Year ' + str(year) + ' - Semester ' + str(semester), ' = $', 
                  format(current_fee, '.2f'), sep='')



# Course coordinator's code:
ORIGINAL_FEE = 8000
YEARLY_PERCENT_INCREASE = 2

# Starting with original fee at start of year 1
fee = ORIGINAL_FEE

# Display fees at the end of year for next five years
for year in range(1, 6):
    # Increase 'fee' variable by the set percentage
    fee = fee * (1 + YEARLY_PERCENT_INCREASE / 100)
    # Display it along with year
    print(year, ' -> $', format(fee, '.2f'), sep='')


