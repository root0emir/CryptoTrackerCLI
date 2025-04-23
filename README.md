# Crypto Tracker CLI

This tool allows you to track the prices of the top 20 cryptocurrencies in real-time from the command line. It works on both Windows and Linux operating systems.

## Features

- Live tracking of top 20 cryptocurrencies
- Market cap, price, 24-hour change, and volume information
- Colorful and organized command-line interface
- Customizable refresh interval

## Requirements

- Python 3.6+
- requests
- tabulate
- colorama
- click

## Installation

1. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Live Tracking

To track cryptocurrency prices in real-time:

```bash
python crypto_tracker.py live
```

To adjust the refresh interval (for example, 30 seconds):

```bash
python crypto_tracker.py live --interval 30
# or
python crypto_tracker.py live -i 30
```

### One-time Display

To display cryptocurrency prices just once:

```bash
python crypto_tracker.py once
```

## Note

This tool uses the CoinGecko API and does not require an API key. However, due to API usage limitations, you should avoid refreshing too frequently.

## Shortcuts

- To terminate the program: `Ctrl+C`
