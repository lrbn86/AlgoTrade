# Grabs stock price from Yahoo Finance 

import urllib
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz
from pytz import timezone
import time
start_capital = 10000
capital = 10000
MAX_BUY_PRICE = 108.72
MAX_SELL_PRICE = 108.72

SIM_STOP_TIME = "08:53:00 PM"
# Eastern Time Zone
MARKET_TIME_CLOSE = "04:00 PM"

STOCK_NAME = "JPY=X"

STOCK_URL = "https://finance.yahoo.com/quote/" + STOCK_NAME

# Get time by first getting UTC and converting to EST
# Used to determine when to stop trading, i.e. stop trading when market closes
def getTime():
    utc = timezone('UTC')
    now = utc.localize(datetime.utcnow())
    est = timezone('US/Eastern')
    local_time = now.astimezone(est).strftime("%H:%M:%S")
    d = datetime.strptime(local_time, "%H:%M:%S").strftime("%I:%M:%S %p")
    return d

def getStockInfo():
    STOCK_URL_PAGE = urllib.request.urlopen(STOCK_URL)
    html = BeautifulSoup(STOCK_URL_PAGE, 'html.parser')
    MAIN_ID = html.find(id="quote-header-info").descendants
    STOCK_INFO = [stock_info.text for stock_info in MAIN_ID if stock_info.name == "span"]
    stock_price = STOCK_INFO[1]
    print("\tPrice: "+stock_price + " @ " + getTime())
    return stock_price

total_cost = 0
total_profit = 0
total_shares = 0
total_shares_bought = 0
total_shares_sold = 0

def strategy1(stock_price, shares):
    current_price = float(stock_price)
    buy_price = 0
    sell_price = 0
    global total_cost
    global capital
    global total_shares
    global total_profit
    global total_shares_bought
    global total_shares_sold
    if current_price < MAX_BUY_PRICE:
        # Buy
        buy_price = current_price
        if capital <= 2200:
            # Hold
            print("\tHolding " + str(total_shares) + " total shares @ total cost of " + str(total_cost))
            return
        total_shares += shares
        total_shares_bought += shares
        cost = shares*buy_price
        total_cost += cost
        capital -= cost
        print("\t*Bought " + str(shares) + " share(s) @ " + str(buy_price) + "*")
    elif current_price >= MAX_SELL_PRICE:
        # Sell
        sell_price = current_price
        if total_shares <= 0:
            print("\t*There are no shares to sell*")
            return
        print("\t*Sold " + str(total_shares) + " shares (total_shares) @ " + str(sell_price) + "*")
        profit = (sell_price - buy_price) * total_shares
        total_shares_sold += total_shares
        total_shares -= total_shares
        capital += profit
        total_profit += profit

def startSimulation():
    global total_profit
    global total_shares
    global total_shares_bought
    global total_shares_sold

    start_time = getTime()
    while getTime() < SIM_STOP_TIME:
        getStockInfo()
        strategy1(getStockInfo(), 2)
        time.sleep(0.1) # Give cpu time to rest
    print("\n\n########################################################################\n")
    print("Simulation started @ " + start_time + " and stopped @ " + SIM_STOP_TIME+ "\n")
    print("Result")
    print("Stock: " + STOCK_NAME)
    print("Start Capital: " + str(start_capital))
    print("End Capital: " + str(capital) + "\n")
    print("Strategy:")
    print("Each trade consist of buying 2 trades and selling all shares")
    print("Buy when price is < " + str(MAX_BUY_PRICE) + " and sell when price is >= " + str(MAX_SELL_PRICE)+"\n")
    print("Remaining shares held: " + str(total_shares))
    print("Total shares bought: " + str(total_shares_bought))
    print("Total shares sold: " + str(total_shares_sold))
    print("Profit realized: " + str(total_profit))
    print("\n########################################################################\n")


def startTrade():
    # The main loop
    while getTime() < market_time_close:
        getTime()
        time.sleep(0.1) # Give cpu time to rest
    print("Market Closed @ " + market_time_close)


print("\n########################################################################\n")
print("\tWelcome to the Stock Price Monitor")
print("\tThe stock of interest is [ " + STOCK_NAME + " ] ")
print("\tLooking at stock price now...\n")
time.sleep(2)
startSimulation()


