import yfinance as yf
import json
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime
import asyncio

# Initialize Console
console = Console()

# Default Configuration
DEFAULT_CONFIG = {
    "global_settings": {
        "max_price": 10.0,
        "min_volume": 100000,
        "time_window": 30,
        "refresh_interval": 10,
    },
    "independent_boxes": {},
    "last_run": {
        "stocks_processed": [],
        "runtime": None,
    },
}


# Load or Create Configuration
def load_config():
    if not os.path.exists("config.json"):
        save_config(DEFAULT_CONFIG)
    with open("config.json", "r") as f:
        return json.load(f)


def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)


# Main Menu
def main_menu():
    while True:
        console.clear()
        console.print(Panel("[bold blue]Stock Bot Main Menu[/bold blue]", title="Welcome"))
        console.print("1. Configure Global Settings")
        console.print("2. Configure Independent Box Settings")
        console.print("3. Run Stock Bot")
        console.print("4. View Last Run Info")
        console.print("5. Help")
        console.print("6. Exit")

        choice = console.input("[bold yellow]Enter your choice (1-6): [/bold yellow]")
        if choice == "1":
            configure_global_settings()
        elif choice == "2":
            configure_independent_boxes()
        elif choice == "3":
            run_stock_bot()
        elif choice == "4":
            view_last_run()
        elif choice == "5":
            help_menu()
        elif choice == "6":
            console.print("[bold green]Exiting. Goodbye![/bold green]")
            break
        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")


# Global Settings Menu
def configure_global_settings():
    config = load_config()
    settings = config["global_settings"]

    console.print(Panel("[bold cyan]Global Settings[/bold cyan]"))
    settings["max_price"] = float(console.input("Set max price: "))
    settings["min_volume"] = int(console.input("Set minimum volume: "))
    settings["time_window"] = int(console.input("Set time window (days): "))
    settings["refresh_interval"] = int(console.input("Set refresh interval (seconds): "))

    config["global_settings"] = settings
    save_config(config)
    console.print("[bold green]Global settings updated![/bold green]")
    console.input("Press Enter to return to the main menu.")


# Independent Box Settings Menu
def configure_independent_boxes():
    config = load_config()
    boxes = config["independent_boxes"]

    console.print(Panel("[bold cyan]Independent Box Settings[/bold cyan]"))
    symbol = console.input("Enter stock symbol for the box: ")
    if symbol not in boxes:
        boxes[symbol] = DEFAULT_CONFIG["global_settings"].copy()

    console.print(f"[bold magenta]Configuring settings for {symbol}[/bold magenta]")
    boxes[symbol]["max_price"] = float(console.input("Set max price: "))
    boxes[symbol]["min_volume"] = int(console.input("Set minimum volume: "))
    boxes[symbol]["time_window"] = int(console.input("Set time window (days): "))
    boxes[symbol]["refresh_interval"] = int(console.input("Set refresh interval (seconds): "))

    config["independent_boxes"] = boxes
    save_config(config)
    console.print(f"[bold green]Settings for {symbol} updated![/bold green]")
    console.input("Press Enter to return to the main menu.")


# View Last Run Info
def view_last_run():
    config = load_config()
    last_run = config["last_run"]

    table = Table(title="Last Run Info")
    table.add_column("Stocks Processed", justify="left")
    table.add_column("Runtime", justify="center")

    stocks = ", ".join(last_run.get("stocks_processed", [])) or "None"
    runtime = last_run.get("runtime", "Never Run")

    table.add_row(stocks, runtime)
    console.print(table)
    console.input("Press Enter to return to the main menu.")


# Help Menu
def help_menu():
    console.clear()
    console.print(Panel("[bold cyan]Help Menu[/bold cyan]", title="Stock Bot Help"))
    console.print("[bold green]1. Global Settings[/bold green]: Configure shared settings for all boxes.")
    console.print("[bold green]2. Independent Box Settings[/bold green]: Configure individual settings for specific stock boxes.")
    console.print("[bold green]3. Running the Bot[/bold green]: Run the stock bot to analyze stocks based on your settings.")
    console.print("[bold green]4. Viewing Last Run Info[/bold green]: See the stocks processed and runtime of the last bot execution.")
    console.print("[bold green]5. About `yfinance`[/bold green]: `yfinance` is a Python library for retrieving financial data from Yahoo Finance.")
    console.print("[bold green]6. Exiting[/bold green]: Quit the application.")
    console.input("Press Enter to return to the main menu.")


# Run Stock Bot
def run_stock_bot():
    config = load_config()
    settings = config["global_settings"]
    boxes = config["independent_boxes"]

    stock_symbols = list(boxes.keys()) or ["AAPL", "MSFT", "GOOGL"]  # Default to some stocks if no independent boxes
    processed_stocks = []

    for symbol in stock_symbols:
        stock_settings = boxes.get(symbol, settings)
        stock_data = fetch_stock_data(symbol, stock_settings)
        processed_stocks.append(symbol)

        console.print(Panel(f"[bold yellow]Stock: {symbol}[/bold yellow]\n" + "\n".join(
            [f"{key}: {value}" for key, value in stock_data.items()]
        )))

    config["last_run"] = {
        "stocks_processed": processed_stocks,
        "runtime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    save_config(config)
    console.print("[bold green]Stock bot run completed![/bold green]")
    console.input("Press Enter to return to the main menu.")


# Fetch Stock Data
def fetch_stock_data(symbol, settings):
    stock = yf.Ticker(symbol)
    hist = stock.history(period=f"{settings['time_window']}d")
    return {
        "Price": hist['Close'][-1],
        "Volume": hist['Volume'][-1],
        "Price Change (%)": (hist['Close'][-1] - hist['Close'][0]) / hist['Close'][0] * 100,
    }


# Entry Point
if __name__ == "__main__":
    main_menu()
