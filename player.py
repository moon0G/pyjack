import os
import random

import pygame

from modl import action
from modl import datastructure as ds
from modl import rules
from modl import gui


dir = os.path.dirname(os.path.realpath(__file__))
cards = rules.cards()
card_data = cards.new()
dealer = action.dealer(card_data)
gui = gui.gui(dir)


deck = ds.array(52) # stack for the deck; simulating actual deck of cards
for key in card_data.keys(): # 
    if key != "cardback":
        deck.apnd(key)

for x in range(1, random.randint(1, 50)): # shuffle deck
    deck.reinit(dealer.shuffle(deck.array)) 

hands, new_deck = dealer.deal(deck.array, 1)
deck.reinit(new_deck)

player_hand = hands.pop()
dealer_hand = hands.pop()

val = 0
for x in dealer_hand:
    try:
        val += card_data[x][1]
    except:
        if val + card_data[x][1][1] > 21:
            val += card_data[x][1][0]
        else:
            val += card_data[x][1][1]

if val > 21:
    gui.display("Game Over", dealer_hand, player_hand)
else:
    gui.display(val, dealer_hand, player_hand)

stat = True
while stat:
    for event in gui.e(): # quit is handled by class
        print(event)
        if str(event) == '<Event(256-Quit {})>':
            stat = False
            break


gui.quit()