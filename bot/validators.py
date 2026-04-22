def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be buy or sell")


def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be in market or limit")


def validate_quantity(qty):
    qty = float(qty)
    if qty <= 0:
        raise ValueError("Quantity much be greater than zero")


def validate_price(price):
    if price is not None:
        price = float(price)
        if price <= 0:
            raise ValueError("Price must be greater than zero")
