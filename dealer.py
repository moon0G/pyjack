from modl import datastructure as ds
from modl import action
from modl import rules
from _thread import *
import threading
import random
import socket


host_sock = ('127.0.0.1', 3000) # bind socket
dealer_sock = socket.socket()
dealer_sock.bind(host_sock)

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

iteration = 0 # iteration
while True:
    if iteration < p: 
        dealer_sock.listen(1)
        conn, addr = dealer_sock.accept()
        
        server.lock.acquire()
        print(f"new connection: {addr}")
        start_new_thread(server.handle_connection, (conn, hands.pop(), dealer_deck[0])) 
    else:
       break  

dealer_sock.close()
