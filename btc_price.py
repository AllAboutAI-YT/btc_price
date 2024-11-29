import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

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

def get_historical_prices(days=7):
    """Fetch historical Bitcoin price data"""
    try:
        url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
        params = {
            'vs_currency': 'usd',
            'days': days,
            'interval': 'daily'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        prices = data['prices']  # Returns [[timestamp, price], ...]
        
        dates = [datetime.fromtimestamp(price[0]/1000) for price in prices]
        prices = [price[1] for price in prices]
        
        return dates, prices
        
    except requests.exceptions.RequestException as e:
        print(f'Error fetching historical prices: {e}')
        return None, None

def plot_bitcoin_price(days=7):
    """Create and display a plot of Bitcoin price history"""
    dates, prices = get_historical_prices(days)
    
    if not dates or not prices:
        return
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(dates, prices, 'b-', linewidth=2)
    
    # Customize the plot
    plt.title('Bitcoin Price History (USD)', fontsize=14, pad=15)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    
    # Format y-axis to show dollar amounts
    def dollar_format(x, p):
        return f'${x:,.0f}'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(dollar_format))
    
    # Format x-axis to show dates nicely
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Calculate and add price change percentage
    if len(prices) >= 2:
        price_change = ((prices[-1] - prices[0]) / prices[0]) * 100
        color = 'green' if price_change >= 0 else 'red'
        plt.text(0.02, 0.95, f'{days}d Change: {price_change:.2f}%', 
                transform=plt.gca().transAxes, color=color,
                bbox=dict(facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()

def main():
    current_data = get_bitcoin_price()
    if current_data:
        print("\nGenerating price history plot...")
        plot_bitcoin_price(days=7)  # Show last 7 days by default

if __name__ == '__main__':
    main()