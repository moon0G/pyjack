import os
import random
import socket

import pygame
from pygame.locals import *

from modl import rules

dir = os.path.dirname(os.path.realpath(__file__))
host_port = ('10.49.230.44', 3000)


cards = rules.cards()
card_data = cards.new()


client_sock = socket.socket()
client_sock.connect(host_port)


pygame.init()
screen = pygame.display.set_mode((640, 360))
font = pygame.font.SysFont('Calibri', 30)


client_sock.send(b'GET HAND')
hand = client_sock.recv(1024).decode().split()
dealer_card = client_sock.recv(1024).decode().split()


val = 0
for x in hand:
    try:
        val += card_data[x][1]
    except:
        if val + card_data[x][1][1] > 21:
            val += card_data[x][1][0]
        else:
            val += card_data[x][1][1]


#display cards
print(dealer_card)
screen.blit(pygame.image.load(dir + '/cards/' + card_data[hand[0]][0]).convert(), (50, 100)) # first card
screen.blit(pygame.image.load(dir + '/cards/' + card_data[hand[1]][0]).convert(), (150, 100)) # second card
screen.blit(pygame.image.load(dir + '/cards/' + card_data[dealer_card[0]][0]).convert(), (250, 100)) # dealers card
screen.blit(pygame.image.load(dir + '/cards/cardback.gif').convert(), (350, 100)) # the other of dealers card turned


if val > 21: 
    screen.blit(font.render('Game Over', False, (255, 255, 255)), (170, 200))
else:
    screen.blit(font.render(f'{val}', False, (255, 255, 255)), (170, 200))


screen.blit(font.render('Dealer', False, (255, 255, 255)), (300, 200))


pygame.display.flip()


status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
 
pygame.quit()

