import os
import random
import socket
import threading
from _thread import *

import pygame

from modl import action
from modl import datastructure as ds
from modl import rules

host_sock = ('127.0.0.1', 3000) # bind socket
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


pygame.init()
screen = pygame.display.set_mode((640, 360))
font = pygame.font.SysFont('Calibri', 30)


val = 0
for x in dealer_deck:
    try:
        val += card_data[x][1]
    except:
        if val + card_data[x][1][1] > 21:
            val += card_data[x][1][0]
        else:
            val += card_data[x][1][1]


screen.blit(pygame.image.load(dir + '/cards/' + card_data[dealer_deck[0]][0]).convert(), (50, 100))
screen.blit(pygame.image.load(dir + '/cards/' + card_data[dealer_deck[1]][0]).convert(), (150, 100))


if val > 21:
    screen.blit(font.render('Game Over', False, (255, 255, 255)), (170, 200))
else:
    screen.blit(font.render(f'{val}', False, (255, 255, 255)), (170, 200))

pygame.display.flip()

stat = True
while stat:
    #for i in pygame.event.get():
    #    if i.type == pygame.QUIT:
    #        stat = False  
    
    try:
        dealer_sock.listen(1)
        conn, addr = dealer_sock.accept()
       
        server.lock.acquire()
        print(f"new connection: {addr}")
        start_new_thread(server.handle_connection, (conn, hands.pop(), dealer_deck[0])) 
        
    except:
        pass

dealer_sock.close()
pygame.quit()
quit()
