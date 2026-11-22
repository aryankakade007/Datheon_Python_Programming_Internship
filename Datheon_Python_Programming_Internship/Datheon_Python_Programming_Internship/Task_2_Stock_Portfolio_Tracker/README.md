# Stock Portfolio Performance Tracker

A simple Python project that tracks stock investments, calculates portfolio performance, displays a summary, and saves performance logs to a CSV file.

## Features

- Validates stock ticker symbols using the S&P 500 constituents dataset.
- Accepts ticker, purchase price, quantity, and current price.
- Calculates invested capital, market value, gain/loss, and gain/loss percentage.
- Displays a formatted portfolio summary in the console.
- Saves timestamped portfolio records to `portfolio_summary.csv`.
- Handles invalid tickers and non-numeric inputs.

## Technologies Used

- Python 3
- CSV module
- Datetime module

## Project Files

- `portfolio.py` — Main application script.
- `constituents.txt` — S&P 500 ticker and company dataset.
- `portfolio_summary.csv` — Generated portfolio performance log.

## How to Run

1. Make sure Python 3 is installed.
2. Keep `portfolio.py` and `constituents.txt` in the same folder.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python portfolio.py

   ## Internship Task

**Task 2:** Stock Portfolio Performance Tracker

**Organization:** Datheon — AI Systems & Automation Studio

**Program:** Python Programming Internship