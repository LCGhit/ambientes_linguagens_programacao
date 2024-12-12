import pdb
import re
import requests
from bs4 import BeautifulSoup

# URL for the updated Yahoo Finance Crypto page
url = 'https://finance.yahoo.com/markets/crypto/all/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the cryptocurrency data
    table = soup.find('table', {'class': 'markets-table freeze-col yf-paf8n5 fixedLayout'})

    pdb.set_trace()
    if table:
        # Iterate through each row in the table (excluding the header row)
        rows = table.find_all('tr')[1:]

        # Extract and print the desired data from each row
        for row in rows:
            columns = row.find_all('td')

            # Ensure we have the correct number of columns (6 columns)
            if len(columns) >= 6:
                name = columns[0].get_text(strip=True)
                symbol = columns[1].get_text(strip=True)
                market_cap = columns[3].get_text(strip=True)
                values = re.split(r'\+', market_cap)
                price = values[0]
                change = ''
                volume = columns[5].get_text(strip=True)

                # Print the extracted information
                print(f"Name: {name}, Symbol: {symbol}, Price: {price}, Change: {change}, Market Cap: {market_cap}, Volume: {volume}")
    else:
        print("Could not find the table containing cryptocurrency data.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
