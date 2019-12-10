# Grabs stock price from Yahoo Finance on their title.
import urllib
from bs4 import BeautifulSoup
stock_name = "^IXIC"
url = "https://finance.yahoo.com/quote/" + stock_name

def getPrice():
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    m = soup.find_all('span')
    print(m)
    m = m [13:16]
    stock_price = m[0].string
    print(stock_price)

#while True:
#    getPrice()

while True:
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    m = soup.find(id="quote-header-info").descendants
    n = [d.text for d in m if d.name == "span"]
    stock_price = n[1]
    print(stock_price)
