import csv
import pandas as pd

# Signals
# Sharpe Ratio - The higher, the attractive
# = (R_p - R_f) / o_p
# R_p = return of portfolio
# R_f = risk-free rate
# o_p = standard deviation of portfolio's excess return

total_returns = 0

total_open_price = 0
total_high_price = 0
total_low_price = 0
total_close_price = 0
total_adj_close_price = 0

df = pd.read_csv('TWTR.csv')
first_date = df['Date'].values[0]
last_date = df['Date'].values[-1]

open_prices = []
high_prices = []
low_prices = []
close_prices = []
adj_close_prices = []

with open('TWTR.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    # ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    #   row0,   row1,   row2,   row3,  row4,    row5,        row6
    for row in csv_reader:
        open_price      = float(row[1])
        high_price      = float(row[2])
        low_price       = float(row[3])
        close_price     = float(row[4])
        adj_close_price = float(row[5])
        open_prices.append(open_price)
        high_prices.append(high_price)
        low_prices.append(low_price)
        close_prices.append(close_price)
        adj_close_prices.append(adj_close_price)

avg_open_price = sum(open_prices) / len(open_prices)
avg_high_price = sum(high_prices) / len(high_prices)
avg_low_price = sum(low_prices) / len(low_prices)
avg_close_price = sum(close_prices) / len(close_prices)
avg_adj_close_price = sum(adj_close_prices) / len(adj_close_prices)

print()
print("****")
print("FOR TWTR stock")
print("Between " + first_date + " and " + last_date + ":")
print("The average open price was " + str(avg_open_price))
print("The average high price was " + str(avg_high_price))
print("The average low price was " + str(avg_low_price))
print("The average close price was " + str(avg_close_price))
print("The average adjusted close price was " + str(avg_adj_close_price))
print("****")
print()

print("Enter starting capital: ", end="")
capital = input()
total_shares = 0
print("My starting capital: " + capital + " in USD")
capital = int(capital)
print("Enter shares: ", end="")
shares = input()
print("If I were to buy a fixed shares of " + str(shares) + "...")
shares = int(shares)
for price in close_prices:
    if price < avg_close_price:
        # Buy
        capital -= price*shares
        total_shares += shares
    elif price > avg_close_price:
        # Sell
        capital += price*total_shares
        total_shares -= total_shares

print("After applying strategy, my current capital would be: " + str(capital))
#print("My total returns would be: " + str(total_returns))dd
