
'''
Write a program that uses nested loops to collect data and calculate the 
average rainfall over a period of years. The program should first ask for 
the number of years. The outer loop will iterate once for each year. The 
inner loop will iterate twelve times, once for each month. Each iteration 
of the inner loop will ask the user for the millimetres of rainfall for that 
month. After all iterations, the program should display the number of months, 
the total millimetres of rainfall, and the average rainfall per month for 
the entire period.
'''

# Get the number of years for rainfall period
years = int(input('Enter the number of years of rainfall: '))

# Use a List to store the months for display output only
lst_months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']

# Accumulator for summing the rainful each month
total_mms = 0.00

for year in range(1, years+1):

    print('YEAR ' + str(year) + '\n' + '-'*20)
    
    for month in range(12):

        total_mms += float(input('Enter the millimetres of rainfall for ' \
                          + lst_months[month] + ': '))
        
total_months = years * 12
avg_rainfull = total_mms / total_months
            
print('Total Rainfall in mms: ', format(total_mms, '.3f'), 'mm')
print('Total months recorded: ', total_months)
print('Average rainfall per month = ', format(avg_rainfull, '.3f'), 'mm')    
    



# Course coordinator's code:
year_count = int(input('How many years of rainfall data is available? '))

total_rainfall = 0  # accumulator variable
average_per_month = 0

for year in range(1, year_count+1):
    print('\n*** Data input for year', year, '***')
    for month in range(1, 13):
        month_data = float(input('Enter rainfall millimeters for month ' + str(month) + ': '))
        total_rainfall += month_data

total_months = year_count * 12
average_per_month = total_rainfall / total_months

print('\nYou provided data for', total_months, 'months.')
print('Total rainfall millimeters for entire period is', total_rainfall)
print('Monthly average for that period is', average_per_month)
