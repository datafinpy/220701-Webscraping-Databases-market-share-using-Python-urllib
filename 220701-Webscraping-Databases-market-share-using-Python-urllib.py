# Importing required libraries
from urllib.request import Request, urlopen
import pandas as pd

# Define the target url
url = "https://www.datanyze.com/market-share/databases--272"

# Define headers parameters, which help us avoid urllib.error.HTTPError: HTTP Error 403: Forbidden
headers = {'User-Agent': 'Mozilla/5.0',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Create the connection
request_site = Request(url, headers=headers)
# Read the information
webpage = urlopen(request_site).read()
# If you want to check the data received in text mode
print(webpage[:150])
# Use pandas to read the table in the html webpage. We use [0], as we want the first table
df = pd.read_html(webpage)[0]
# Use the 'Ranking' column as index
df.set_index('Ranking', drop=True, inplace=True)
# We modify how pandas shows the information, to allow all the columns to appear
pd.set_option('display.max_columns', None)
# Show the data
print(df)
