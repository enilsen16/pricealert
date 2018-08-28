from __future__ import print_function

import json
import os
import signal
import socket
import sys
import time

import cbpro
import requests
import requests_oauthlib

def send_to_wallaroo(msg, tcp_connection):
    try:
        tcp_connection.sendall(str(len(msg) + 1).zfill(5) +
                               msg + '\n')
    except:
        print "Error decoding data received from Coinbase!"

class coinbaseWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD"]
        self.message_count = 0
        print("Lets count the messages!")

    def on_message(self, msg):
        if 'price' in msg and 'type' in msg:
            self.message_count += 1
            send_to_wallaroo(msg, sock)
            print("Message type:", msg["type"],
                  "\t@ {:.3f}".format(float(msg["price"])))

    def on_close(self):
        print("-- Goodbye! --")
s
print("Set up Coinbase websocket....")
wsClient = coinbaseWebsocketClient()
wsClient.start()

print("Set up Wallaroo socket.....")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wallaro_input_address = ('localhost', 8002)

print 'connecting to Wallaroo on %s:%s' % wallaro_input_address
sock.connect(wallaro_input_address)

print(wsClient.url, wsClient.products)
while (wsClient.message_count < 500):
    print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
    time.sleep(0.5)
wsClient.close()
