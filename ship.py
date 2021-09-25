import pygame
class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("data/x_wing.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right=False
        self.moving_left=False
        self.settings = ai_game.settings
        self.x = self.rect.x
        
    def blitme(self):
        '''Draw a ship in a current location:'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.x>0:
            self.x -= self.settings.ship_speed
        else:
            self.x=self.x

        self.rect.x=self.x