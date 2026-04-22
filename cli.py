import argparse
from bot.clients import get_client
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.qty)
    validate_price(args.price)

    if args.type == "LIMIT" and not args.price:
        raise ValueError("LIMIT order requires --price")

    client = get_client()

    print("Placing Order...")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.qty)

    if args.price:
        print("Price:", args.price)

    result = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

    print("\nSUCCESS")
    print("Order ID:", result["orderId"])
    print("Status:", result["status"])
    print("Executed Qty:", result["executedQty"])

except Exception as e:
    print("\nFAILED:", e)