from __future__ import print_function
import socket
import sys
import requests
import requests_oauthlib
import json
import os

import gdax, time

import signal
import sys

def send_to_wallaroo(msg, tcp_connection):
    try:
        price_text = msg["price"].encode('utf-8')
        tcp_connection.sendall(str(len(price_text)+1).zfill(5) +
                price_text + '\n')
    except:
        print "Error decoding data received from Coinbase!"

class coinbaseWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com"
        self.products = ["BTC-USD"]
        self.message_count = 0

    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            send_to_wallaroo(msg, sock)
            print("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))

    def on_close(self):
        print("-- Goodbye! --")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wallaro_input_address = ('localhost', 8002)

print 'connecting to Wallaroo on %s:%s' % wallaro_input_address
sock.connect(wallaro_input_address)

wsClient = coinbaseWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products)

while (wsClient.message_count < 1000):
    time.sleep(1)

wsClient.close()
