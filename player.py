import os
import random
import time
import sys
from datetime import datetime

import pygame
from pygame.locals import *
pygame.init()

from modl import action
from modl import datastructure as ds
from modl import rules
from modl import gui

# loop for gathering wager
for i in sys.argv:
    if i=="-$":
        wager = int(sys.argv[sys.argv.index(i)+1]) # set wager
        break
    else:
        wager = 100 # default wager = 100

start_time = datetime.now().strftime("(%d/%b/%Y @ %H:%M:%S)")

turn = True # loading all the variables
stood = False
dir = os.path.dirname(os.path.realpath(__file__))
cards = rules.cards()
card_data = cards.new()
dealer = action.dealer(card_data, dir)
gui = gui.gui(dir)
last_pos = [75, 100]
dlast_pos = [375, 100]

deck = ds.array(52) # stack for the deck; simulating actual deck of cards
for key in card_data.keys(): # 
    if key != "cardback":
        deck.apnd(key)

for x in range(1, random.randint(1, 50)): # shuffle deck
    deck.reinit(dealer.shuffle(deck.array)) 

hands, new_deck = dealer.deal(deck.array, 1) # deal cards
deck.reinit(new_deck)

player_hand = hands.pop() # dealer and player hands 
dealer_hand = hands.pop() 

val = dealer.calculate_weight(player_hand, card_data) # calculate weight of the cards


if val > 21:
    gui.display("Game Over", dealer_hand, player_hand)
else:
    gui.display(val, dealer_hand, player_hand)


stat = True
while stat:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stat = False
            break
            
        elif turn == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                
                if (pos[0] < 50 and pos[0] > 0) and (pos[1] < 50 and pos[1] > 0): # hit button
                    new_card, new_deck = dealer.hit(deck.array)
                    deck.reinit(new_deck)
                    del new_deck

                    player_hand.append(new_card)
                    val = dealer.calculate_weight(player_hand, card_data)

                    if val > 21:
                        stood = True

                    gui.add_card(new_card, (last_pos[0]+25, last_pos[1]))
                    last_pos[0] += 25

                    #if val > 0:
                        #gui.update_score(val, (60, 200))

                    turn = False

                if (pos[0] < 100 and pos[0] > 50) and (pos[1] > 0 and pos[1] < 50): #
                    turn = False
                    stood = True
                    continue

    if turn == False: # dealer logic - turn = False = dealers turn
        dealer_val = dealer.calculate_weight(dealer_hand, card_data)

        if dealer_val >= 17 or dealer_val < 0: # dealer will stay
            if dealer_val <= 21 and dealer_val > val and stood:
                gui.end_scr(dealer_hand, player_hand, dealer_val, val)
                wager *= -1
                time.sleep(5)
                stat = False
            elif stood:
                gui.end_scr(dealer_hand, player_hand, dealer_val, val)
                wager *= 2
                time.sleep(5)
                stat = False
            
            if not stood:
                turn = True

        elif dealer_val <= 16 and dealer_val > 0: # dealer will hit
            new_card, new_deck = dealer.hit(deck.array)
            deck.reinit(new_deck)
            del new_deck

            dealer_hand.append(new_card)

            dealer_val = dealer.calculate_weight(dealer_hand, card_data)

            if not stood:
                turn = True
            gui.add_card(new_card, (dlast_pos[0]+25, dlast_pos[1]))
            last_pos[0] += 25
        
        else:
            pass
        
    gui.turn(turn)
    time.sleep(12/1000)

gui.quit()
if not turn:
    dealer.write_out("score", start_time, wager)