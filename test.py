import os
import wget
import requests

curr_dir = os.getcwd()
url = 'https://query1.finance.yahoo.com/v7/finance/download/SRET?period1=1544439929&period2=1575975929&interval=1d&events=history&crumb=2RzFxVmgvZk'

myfile = requests.get(url)
open('SRET.csv', 'wb').write(myfile.content)

# Cannot download from Yahoo API, sad... but that's okay. I need to reserach the stocks on my own anyways