# Binance Futures Testnet Trading Bot

A command-line Python trading bot built for the Primetrade.ai Python Developer assignment.

This application connects to Binance Futures Testnet / Demo Futures API and places MARKET and LIMIT orders using Python.

---

# Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* CLI input using argparse
* Input validation
* Logging to file
* Error handling
* Structured reusable code

---

# Project Structure

```text
trading_bot/
│── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│── logs/
│── cli.py
│── .env
│── requirements.txt
│── README.md
```

---

# Requirements

* Python 3.9+
* pip
* Binance Demo/Testnet Account
* API Key + Secret

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <your-github-repository-link>
cd trading_bot
```

---

## 2. Create Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create `.env` File

Create a file named `.env` in the root folder and add:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

# Binance Endpoint Used

```text
https://demo-fapi.binance.com/fapi
```

---

# Run Commands

## MARKET BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## MARKET SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

## LIMIT BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## LIMIT SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

# CLI Parameters

| Parameter  | Required   | Example        |
| ---------- | ---------- | -------------- |
| --symbol   | Yes        | BTCUSDT        |
| --side     | Yes        | BUY / SELL     |
| --type     | Yes        | MARKET / LIMIT |
| --quantity | Yes        | 0.001          |
| --price    | LIMIT only | 50000          |

---

# Example Output

```text
Placing Order...
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

SUCCESS
Order ID: 123456789
Status: FILLED
Executed Qty: 0.001
```

---

# Logging

Logs are stored in:

```text
logs/trading.log
```

Logs include:

* API requests
* API responses
* Errors

---

# Error Handling

The application handles:

* Invalid side
* Invalid order type
* Missing price for LIMIT order
* Timestamp mismatch
* Invalid API credentials
* Precision errors
* Insufficient margin
* Minimum notional errors
* Network/API failures

---

# Assumptions

* User has valid Binance Demo/Testnet credentials
* User has sufficient demo balance
* Internet connection is active

---

# Notes

During testing, Binance exchange-side validations such as precision filters, minimum notional checks, and margin checks were handled successfully.

---

# Author

Aman
