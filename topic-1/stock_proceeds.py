# Quantity of shares(units) purchased and sold
num_units_buy = 500
num_units_sell = 500

# Price paid and sold per share
price_per_unit_buy = 25.04
price_per_unit_sell = 36.06

# Incoming proceeds and outgoings excluding commission
price_paid = num_units_buy * price_per_unit_buy
receivings = num_units_sell * price_per_unit_sell

# Brokerage for transactions
brokerage_buy = 0.023 * price_paid
brokerage_sell = 0.021 * receivings
total_commission = brokerage_buy + brokerage_sell

# Net calculation incl. commission fees
net_calc = float(receivings - price_paid - total_commission)

# lambda expression to determine Profit or Loss
p_or_l = lambda x: 'Profit: $' if net_calc >= 0.0 else 'Loss: -$'

print('BUY')
print('Price paid for stock', format(price_paid, '.2f'), sep=': $')
print('Brokerage fees', format(commission_buy, '.2f'), sep=': $')

print('\nSELL')
print('Receivings on sale of stock', format(receivings, '.2f'), sep=': $')
print('Brokerage fees', format(commission_sell, '.2f'), sep=': $')

print(f"\nNet {p_or_l(net_calc)}{abs(net_calc):,.2f}")
