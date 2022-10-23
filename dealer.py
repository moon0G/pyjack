import os
import random
import socket
import threading
from _thread import *

import pygame

from modl import action
from modl import datastructure as ds
from modl import rules
from modl import gui

host_sock = ('10.49.230.44', 3000) # bind socket
dealer_sock = socket.socket()
dealer_sock.bind(host_sock)


dir = os.path.dirname(os.path.realpath(__file__))


server = action.server(threading.Lock()) # server class


cards = rules.cards() # class for card data
card_data = cards.new() # creates new card data
dealer = action.dealer(card_data) # init dealer class


deck = ds.array(52) # stack for the deck; simulating actual deck of cards
for key in card_data.keys(): # 
    if key != "cardback":
        deck.apnd(key)


for x in range(1, random.randint(1, 50)): # shuffle deck
    deck.reinit(dealer.shuffle(deck.array)) 

p = int(input("How many people (excluding you) will be connecting? "))
hands, new_deck = dealer.deal(deck.array, p)
deck.reinit(new_deck)


dealer_deck = hands.pop() # pop out the dealers deck



val = 0
for x in dealer_deck:
    try:
        val += card_data[x][1]
    except:
        if val + card_data[x][1][1] > 21:
            val += card_data[x][1][0]
        else:
            val += card_data[x][1][1]

print(dealer_deck)
gui = gui.dealergui((640, 360), dir)
threading.Thread(target=gui.run, args=(dealer_deck, val), daemon=True).start()


stat = True
while stat:
    try:
        dealer_sock.listen(1)
        conn, addr = dealer_sock.accept()

        server.lock.acquire()
        print(f"new connection: {addr}")
        threading.Thread(target=server.handle_connection, args=(conn, hands.pop(), dealer_deck[0]), daemon=True).start() # start daemonic thread

    except:
        pass

dealer_sock.close()
quit()
