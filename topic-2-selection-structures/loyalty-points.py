# Loyalty points depending on sales amount
LOYAL_PTS_1 = 10
LOYAL_PTS_2 = 20
LOYAL_PTS_3 = 50

SALES_GROUP1_MAX = 100
SALES_GROUP2_MAX = 500

# rounded figure to nearest integer
total_sales = round(float(input("Enter total sales amount: $")))
print(total_sales)
 

if  0 <= total_sales <= SALES_GROUP1_MAX: # can also be: total_sales >= 0 and total_sales <= SALES_GROUP1_MAX
    points = LOYAL_PTS_1
elif SALES_GROUP1_MAX < total_sales <= SALES_GROUP2_MAX:
    points = LOYAL_PTS_2
elif total_sales > SALES_GROUP2_MAX:
    points = LOYAL_PTS_3
else:
    print('Oops. Invalid amount entered')
    
print('You earned', points, 'points')
