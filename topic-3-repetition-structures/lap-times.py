'''
Write a program that asks the user to enter the number of times that they 
have run around a racetrack, and then uses a loop to prompt them to enter 
the lap time for each of their laps. When the loop finishes, the program 
should display the time of their fastest lap, the time of their slowest lap,
and their average lap time
'''

# Import numpy library to use the average function.
import numpy

# Get the number of laps ran.
lap_count = int(input('Enter the number of laps around racetrack: '))

lst_lap_times = [] # initialise a list to hold lap times.

# Loop through all laps and get lap time for each
for i in range(1, lap_count+1):

    lap_time = float(input('Enter the time for lap #' + str(i) + ' = '))
    lst_lap_times.append(lap_time)

# Display slowest, fastest and average times using min, max and average functions
print('The slowest lap was: ', format(max(lst_lap_times), '.2f'), 'mins')
print('The fastest lap was: ', format(min(lst_lap_times), '.2f'), 'mins')
print('The average lap time was: ', format(numpy.average(lst_lap_times), '.2f'), 'mins')




# Course coordinator's code:
laps = int(input('How many laps did you run? '))

min_lap_time = 1000  # set to an unreasonably high value
max_lap_time = 0
total = 0

for lap_number in range(1, laps+1):
    current_lap_time = float(input('Enter time (in minutes) for lap #' + str(lap_number) + ': '))

    # Update the running sum
    total += current_lap_time

    # Update the running minimum nad maximum
    if current_lap_time < min_lap_time:
        min_lap_time = current_lap_time

    if current_lap_time > max_lap_time:
        max_lap_time = current_lap_time

print('\nYour fastest lap completed in', min_lap_time, 'minutes.')
print('Your slowest lap completed in', max_lap_time, 'minutes.')

average_time = total / laps
print('Average lap time is', format(average_time, '.2f'), 'minutes')

