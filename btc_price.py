import requests
from datetime import datetime

def get_bitcoin_price():
    """Fetch Bitcoin price data from CoinGecko API"""
    try:
        # CoinGecko API endpoint for Bitcoin price in USD and NOK
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd,nok',
            'include_24hr_change': 'true',
            'include_24hr_vol': 'true',
            'include_market_cap': 'true'
        }
        
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the response
        data = response.json()['bitcoin']
        
        # Extract relevant information
        current_price_usd = data['usd']
        current_price_nok = data['nok']
        price_change_24h_usd = data['usd_24h_change']
        price_change_24h_nok = data['nok_24h_change']
        market_cap_usd = data['usd_market_cap']
        market_cap_nok = data['nok_market_cap']
        
        # Format the output
        print(f'Bitcoin Price Information - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        print('USD Information:')
        print(f'Current Price: ${current_price_usd:,.2f}')
        print(f'24h Change: {price_change_24h_usd:.2f}%')
        print(f'Market Cap: ${market_cap_usd:,.2f}\n')
        
        print('NOK Information:')
        print(f'Current Price: {current_price_nok:,.2f} NOK')
        print(f'24h Change: {price_change_24h_nok:.2f}%')
        print(f'Market Cap: {market_cap_nok:,.2f} NOK')
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f'Error fetching Bitcoin price: {e}')
        return None

def main():
    get_bitcoin_price()

if __name__ == '__main__':
    main()