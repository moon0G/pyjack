import pygame
from pygame.locals import *
 
class gui: #
    def __init__(self, dir):
        self.dir = dir
        
        self.screen = pygame.display.set_mode((640, 360))
        self.font = pygame.font.SysFont('Calibri', 30)

        
    def display(self, stat: str, dealer_hand: list, cards: list):
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + cards[0] + '.gif').convert(), (50, 100))
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + cards[1] + '.gif').convert(), (75, 100))
        #self.screen.blit(self.font.render(f'{stat}', False, (255, 255, 255)), (60, 200))
    
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + dealer_hand[0] + '.gif').convert(), (350, 100))
        self.screen.blit(pygame.image.load(self.dir + '/cards/cardback.gif').convert(), (375, 100))
        #self.screen.blit(self.font.render('Dealer Hand', False, (255, 255, 255)), (360, 200))

        pygame.draw.rect(self.screen, (0xF5, 0, 0), pygame.Rect(0, 0, 50, 50))

        pygame.draw.rect(self.screen, (0, 0, 0xF5), pygame.Rect(50, 0, 50, 50))

        pygame.display.flip()

    def add_card(self, card: str, xy: tuple):
        self.screen.blit(pygame.image.load(self.dir + '/cards/' + card + '.gif').convert(), xy)

        pygame.display.flip()
    
    def update_score(self, score: int, xy: tuple):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(xy[0], xy[1], 100, 100))
        self.screen.blit(self.font.render(f'{score}', False, (255, 255, 255)), xy)

        pygame.display.flip()
        
    def turn(self, turn: bool):
        if turn:
            self.screen.blit(self.font.render(f'Your Turn!', False, (255, 255, 255)), (485, 300))
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(485, 300, 200, 200))
        
        pygame.display.flip()
        
    def end_scr(self, dealer_hand, player_hand, dealer_val, player_val):
        factor = 50

        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 640, 360))

        stat = ['', '(bust)'][player_val > 21]

        self.screen.blit(self.font.render(f'{player_val} ' + stat, False, (255, 255, 255)), (factor, 200))
        
        for card in player_hand:
            self.screen.blit(pygame.image.load(self.dir + '/cards/' + card + '.gif').convert(), (factor, 25))
            factor += 25
        
        factor += 75
        
        stat = ['', '(bust)'][dealer_val > 21]

        self.screen.blit(self.font.render(f'{dealer_val} ' + stat, False, (255, 255, 255)), (factor, 200))

        for card in dealer_hand:
            self.screen.blit(pygame.image.load(self.dir + '/cards/' + card + '.gif').convert(), (factor, 25))
            factor += 25

        if dealer_val > player_val and dealer_val <= 21:
            self.screen.blit(self.font.render(f'You lose!', False, (255, 255, 255)), (485, 300))
        elif player_val <= 21:
            self.screen.blit(self.font.render(f'You win!', False, (255, 255, 255)), (485, 300))


        pygame.display.flip()

    def quit(self):
        pygame.quit()
