import logging


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }
        if order_type == "LIMIT":
            params["price"] == price
            params["timeInForce"] = "GTC"

        logging.info(f"Sending order request : {params}")
        response = client.future_create_order(**params)
        logging.info(f"Order response : {response}")
        return response
    except Exception as e:
        logging.error(f"Order failed : {str(e)}")
        raise
