from modl import rules
import os
import random
import pygame
from pygame.locals import *
import socket


dir = os.path.dirname(os.path.realpath(__file__))
host_port = ('127.0.0.1', 3000)
pos = [(50, 100), (100, 100), (70, 200), (200, 100), (250, 100), (225, 200)]


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
screen.blit(pygame.image.load(dir + '/cards/' + card_data[hand[0]][0]).convert(), pos[0]) # first card
screen.blit(pygame.image.load(dir + '/cards/' + card_data[hand[1]][0]).convert(), pos[1]) # second card
screen.blit(pygame.image.load(dir + '/cards/' + card_data[dealer_card[0]][0]).convert(), pos[3]) # dealers card
screen.blit(pygame.image.load(dir + '/cards/cardback.gif').convert(), pos[4]) # the other of dealers card turned


if val > 21: 
    screen.blit(font.render('Game Over', False, (255, 255, 255)), pos[2])
else:
    screen.blit(font.render(f'{val}', False, (255, 255, 255)), pos[2])


screen.blit(font.render('Dealer', False, (255, 255, 255)), pos[4])


pygame.display.flip()


status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
 
pygame.quit()

