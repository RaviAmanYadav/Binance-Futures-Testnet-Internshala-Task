import os
import time
from dotenv import load_dotenv
from binance.client import Client


def get_client():
    load_dotenv(".env")

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"
    server_time = client.get_server_time()["serverTime"]
    local_time = int(time.time() * 1000)
    client.timestamp_offset = server_time - local_time

    return client
