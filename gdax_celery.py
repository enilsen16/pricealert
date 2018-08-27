from __future__ import print_function
import django
import os

# This is needed because we are running this outside of django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pricealert.settings")
django.setup()

from djmoney.money import Money
from pricealertweb.models import MarketData
import gdax, time

class coinbaseWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com"
        self.products = ["BTC-USD"]
        self.message_count = 0

    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            MarketData.objects.create(
                price=Money(msg["price"], 'USD')
            )
            print("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))

    def on_close(self):
        print("-- Goodbye! --")

wsClient = coinbaseWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products)
while (wsClient.message_count < 1000):
    time.sleep(1)
wsClient.close()
