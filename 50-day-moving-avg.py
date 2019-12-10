# This program will use the Trend-following strategy
# Specifically, it will use the 50-day moving averages
# created by Brandon Nguyen (lrbn86@gmail.com)

# The 50-day moving average is calculated by summing up the past 50 data points
# and then dividing the result by 50

# If the price is above a moving average, the trend is up
# If the price is below a moving average, the trend is down

# 1. Sum up the 50 most recent daily closing prices and divide by 50 to get 
# new average per day. (SMA)


import csv

print("Enter starting capital: ", end="")
capital = int(input())

opening_prices = []
high_prices = []
low_prices = []
closing_prices = []

with open('TWTR.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        opening_price = float(row[1])
        opening_prices.append(opening_price)
        high_price = float(row[2])
        high_prices.append(high_price)
        low_price = float(row[3])
        low_prices.append(low_price)
        closing_price = float(row[4])
        closing_prices.append(closing_price)

# Sum up the 50 most recent closing prices
sum_of_50_closing_prices = sum(closing_prices[-50:])

# Divide by 50
sma = sum_of_50_closing_prices / 50

print("The moving average is: " + str(sma))

# The first thing that we look at is the opening price for the day
for price in opening_prices:
    
