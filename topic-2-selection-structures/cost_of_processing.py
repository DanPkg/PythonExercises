# Calculate Word processing labour costs
def cost_of_processing():
    
    TYPE_SPEED_WPM = 30
    
    LABOUR_COST_LOWER = 21.75 # Under 8 hours work or less
    LABOUR_COST_UPPER = 25.00 # Over 8 hours work rate
    
    num_of_words = int(input("Number of words to be typed: "))
    
    hours_to_type = (num_of_words / TYPE_SPEED_WPM) / 60
    
    if hours_to_type <= 8:
        labour_charge = LABOUR_COST_LOWER * hours_to_type
    else:
        labour_charge = LABOUR_COST_UPPER * hours_to_type
    
    print('Hours of labour required: ', format(hours_to_type, '.2f'),
          'hours')
    
    print('Labour charges: $', format(labour_charge, '.2f'), sep='')
    
cost_of_processing()
