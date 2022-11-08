import pygame
from pygame.locals import *
 
class gui: #
    def __init__(self, dir):
        self.dir = dir
        
        pygame.init()
        self.screen = pygame.display.set_mode((640, 360))
        self.font = pygame.font.SysFont('Calibri', 30)

        
    def display(self, stat: str, dealer_hand: list, cards: list):
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + cards[0] + '.gif').convert(), (50, 100))
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + cards[1] + '.gif').convert(), (75, 100))
        self.screen.blit(self.font.render(f'{stat}', False, (255, 255, 255)), (60, 200))

        self.screen.blit(pygame.image.load(self.dir + '/cards/' + dealer_hand[0] + '.gif').convert(), (350, 100))
        self.screen.blit(pygame.image.load(self.dir + '/cards/cardback.gif').convert(), (375, 100))
        self.screen.blit(self.font.render('Dealer Hand', False, (255, 255, 255)), (360, 200))

        pygame.display.flip()

    def add_card(self, card: str, xy: tuple):
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + card + '.gif').convert(), xy)

        pygame.display.flip()

    def e(self):
        return pygame.event.get()
        
    def quit(self):
        pygame.quit()