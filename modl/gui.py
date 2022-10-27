import pygame
import time
from pygame.locals import *

class dealergui:
    def __init__(self, dimen: list, dir: str):
        pygame.init()

        self.screen = pygame.display.set_mode(dimen)
        self.font = pygame.font.SysFont('Calibri', 30)
        self.dir = dir

    def __load(self, cards: list, card_val: int) -> None:
        print(cards[0])
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + cards[0] + '.gif').convert(), (100, 100))
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + cards[1] + '.gif').convert(), (50, 100))

        if card_val > 21:
            self.screen.blit(self.font.render('Game Over', False, (255, 255, 255)), (170, 200))
        else:
            self.screen.blit(self.font.render(f'{card_val}', False, (255, 255, 255)), (170, 200))

        pygame.display.flip()

         

    def run(self, cards, val) -> None:
        self.__load(cards, val)

        stat = True
        while stat:
            events = pygame.event.get()
            for i in events:
                if i.type == pygame.QUIT:
                    stat = False

            #pygame.display.flip()
            #time.sleep(60/1000)

    