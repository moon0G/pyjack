import pygame
from pygame import *
import random
import os
from modl import datastructure as ds
from modl import rules
from modl import action

dir = os.path.dirname(os.path.realpath(__file__))

pygame.init()

cards = rules.cards()

screen = pygame.display.set_mode((640, 360))
font = pygame.font.SysFont('Calibri', 30)

card_data = cards.new()
deck = ds.array(52)

for key in card_data.keys():
    if key != "cardback":
        deck.apnd(key)

dealer = action.dealer(card_data)

for x in range(1, random.randint(1, 50)):
    deck.reinit(dealer.shuffle(deck.array))

hands, new_deck = dealer.deal(deck.array, 1)
deck.reinit(new_deck)

## here add part for ace card (1, 11)

val = 0
for x in hands:
    for y in x:
            try:
                val += card_data[y][1]
            except:
                if card_data[y][1][1] + val > 21:
                    val += card_data[y][1][0]
                else:
                    val += card_data[y][1][1]
    break

if val > 21:
    screen.blit(font.render('Game Over'), False, (255, 255, 255), (170, 200))
else:
    screen.blit(font.render(f'{val}', False, (255, 255, 255)), (170, 200))

screen.blit(pygame.image.load(dir + "/cards/" + card_data[hands[0][0]][0]).convert(), (100, 100))
screen.blit(pygame.image.load(dir + "/cards/" + card_data[hands[0][1]][0]).convert(), (200, 100))

pygame.display.flip()

status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
 
pygame.quit()
