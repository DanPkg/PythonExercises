
# OPTION 1 - using dictionary
def show_cost_of_ticket(user_ticket):
        
    # Store cost of each ticket class in a dictionary
    ticket_classes_costs = {
        "A": 50,
        "B": 30,
        "C": 15
    }
    
    return ticket_classes_costs.get(user_ticket)            

user_ticket = str(input("Enter class of ticket (A, B, or C): "))

print('Cost of Ticket Class ', user_ticket + ': $', 
      format(show_cost_of_ticket(user_ticket), '.2f'), sep='')



# OPTION 2 - using decision structure (no error checking)
def show_cost_of_ticket():
    
    CLASS_A_COST = 50
    CLASS_B_COST = 30
    CLASS_C_COST = 15
    
    user_ticket = str(input("Enter class of ticket (A, B, or C): "))
    
    if user_ticket == 'A':
        cost_of_ticket = CLASS_A_COST
    elif user_ticket == 'B':
        cost_of_ticket = CLASS_B_COST
    else:
        cost_of_ticket = CLASS_C_COST        
    
    print('Cost of Ticket Class ', user_ticket + ': $', 
          format(cost_of_ticket, '.2f'), sep='')
        
show_cost_of_ticket()
