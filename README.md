# Bitcoin Price Tracker

A Python application that fetches and visualizes real-time Bitcoin price data using the CoinGecko API. The application displays current prices in USD and NOK, along with market statistics and historical price charts.

## Features

- Real-time Bitcoin price tracking in USD and NOK
- 24-hour price change monitoring
- Market capitalization information
- Historical price visualization with customizable time ranges
- Interactive price charts with percentage change indicators

## Requirements

- Python 3.6+
- Required packages:
  - requests==2.31.0
  - matplotlib
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AllAboutAI-YT/btc_price.git
   cd btc_price
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using Python:
```bash
python btc_price.py
```

The application will:
1. Display current Bitcoin prices in USD and NOK
2. Show 24-hour price changes and market capitalization
3. Generate a price history chart for the last 7 days

## Features in Detail

### Current Price Information
- Real-time price updates in USD and NOK
- 24-hour price change percentage
- Current market capitalization

### Historical Price Visualization
- 7-day price history chart by default
- Price change percentage indicator
- Interactive matplotlib chart with grid lines
- Formatted axes with proper date and price display

## API Integration

This application uses the CoinGecko API to fetch Bitcoin data:
- Current price data: `/simple/price` endpoint
- Historical data: `/coins/bitcoin/market_chart` endpoint

No API key is required for basic usage.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Data provided by [CoinGecko API](https://www.coingecko.com/en/api)
- Built with Python and Matplotlib