print("\n#####################################################################################################\n")
print("Welcome to the Risk/Reward Ratio Calculator\n")
print("To begin, please enter the price of the target stock: ", end="")
buy_stock_price = input()
print("Now, enter the number of shares you will buy at this stock price: ", end="")
num_of_shares = input()
total_cost = float(buy_stock_price) * int(num_of_shares)
print("You are buying " + num_of_shares + " shares of stock at $" + buy_stock_price + ". Total investment of $" + str(total_cost) + "\n")
print("Enter the stock price that you will be willing to sell at: ", end="")
sell_stock_price = input()
msg_result = ""
result = (float(sell_stock_price) - float(buy_stock_price)) * int(num_of_shares)
if result > 0:
    msg_result = ", then you will make a profit of $" + str(result)
elif result < 0:
    msg_result = ", then you will make a loss of $" + str(result)
print("If you sell " + num_of_shares + " shares of stock at $" + sell_stock_price + msg_result + "\n")
ratio = result / total_cost
print("Risk/Reward ratio is " + str(ratio))
print("\n#####################################################################################################\n")
