#!/usr/bin/env python3
import os
import sys
import json
import time
import locale
import requests
from tabulate import tabulate
from colorama import init, Fore, Style
import click

# Colorama init for Windows color support with strip=False to handle Unicode properly
init(strip=False)

# Try to set system locale for better encoding support
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass
    
# Ensure stdout can handle UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        # For Windows, try to set console to utf-8 mode
        if os.name == 'nt':
            os.system('chcp 65001')
    except:
        # If that fails, we'll use ASCII replacement characters
        pass

class CryptoTracker:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3"
        self.update_interval = 60  # Default refresh seconds
        # Extended list is not used as we fetch by market cap directly
        
    def get_crypto_data(self):
        """Fetch cryptocurrency data from CoinGecko API"""
        try:
            # Get top 20 cryptocurrencies by market cap
            url = f"{self.api_url}/coins/markets"
            params = {
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 20,
                "page": 1,
                "sparkline": False,
                "price_change_percentage": "24h"
            }
            
            response = requests.get(url, params=params)
            if response.status_code != 200:
                print(f"{Fore.RED}Error fetching data: {response.status_code}{Style.RESET_ALL}")
                return None
                
            return response.json()
        
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            return None
            
    def display_data(self, data):
        """Display cryptocurrency data in a formatted table"""
        if not data:
            return
            
        table_data = []
        for coin in data:
            price = coin['current_price']
            change_24h = coin['price_change_percentage_24h']
            
            # Colorize price change with ASCII characters
            if change_24h > 0:
                change_display = f"{Fore.GREEN}+ {change_24h:.2f}%{Style.RESET_ALL}"
            else:
                change_display = f"{Fore.RED}- {abs(change_24h):.2f}%{Style.RESET_ALL}"
                
            market_cap = coin['market_cap'] / 1_000_000_000  # Convert to billions
            
            table_data.append([
                coin['market_cap_rank'],
                f"{Fore.CYAN}{coin['name']}{Style.RESET_ALL}",
                f"{Fore.YELLOW}{coin['symbol'].upper()}{Style.RESET_ALL}",
                f"${price:,.2f}",
                change_display,
                f"${market_cap:.2f}B",
                f"${coin['total_volume']:,.0f}"
            ])
            
        headers = ["#", "Name", "Symbol", "Price (USD)", "24h Change", "Market Cap", "24h Volume"]
        table = tabulate(table_data, headers=headers, tablefmt="simple")
        
        # Clear screen and show updated data
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{Fore.MAGENTA}Top 20 Cryptocurrencies by Market Cap{Style.RESET_ALL}")
        print(f"Last Updated: {Fore.BLUE}{time.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
        print(f"\n{table}\n")
        
    def live_tracker(self, interval=None):
        """Start live tracking with specified refresh interval"""
        if interval:
            self.update_interval = interval
            
        print(f"{Fore.CYAN}Starting crypto tracker. Press Ctrl+C to exit.{Style.RESET_ALL}")
        
        try:
            while True:
                data = self.get_crypto_data()
                self.display_data(data)
                print(f"Refreshing in {self.update_interval} seconds. Press Ctrl+C to exit.")
                time.sleep(self.update_interval)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Exiting crypto tracker. Goodbye!{Style.RESET_ALL}")
            sys.exit(0)

@click.group()
def cli():
    """CLI tool for tracking cryptocurrency prices in real-time."""
    pass

@cli.command()
@click.option('--interval', '-i', default=60, help='Refresh interval in seconds (default: 60)')
def live(interval):
    """Start live tracking of top cryptocurrencies."""
    tracker = CryptoTracker()
    tracker.live_tracker(interval)

@cli.command()
def once():
    """Display current cryptocurrency data once without live updates."""
    tracker = CryptoTracker()
    data = tracker.get_crypto_data()
    tracker.display_data(data)

if __name__ == "__main__":
    cli()
