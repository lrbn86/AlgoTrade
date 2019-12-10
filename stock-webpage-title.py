# Grabs stock price from Yahoo Finance 

import urllib
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz
from pytz import timezone
import time

capital = 10000

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
    print("\t"+stock_price + " @ " + getTime())


def strategy1(stock_price):
    print("Do strategy here")

def startSimulation():
    while True:
        getStockInfo()
        time.sleep(0.1) # Give cpu time to rest

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
time.sleep(5)
startSimulation()


