#setting up a game environemnt for Alien Invasion:
#importing system functions:
import sys
#importing pygame:
import pygame
#importing a settings module:
from settings import Settings
#importing a ship:
from ship import Ship

#class for Game Management:
class AlienInvasion:
    """All things concerning game assets and behaviour."""
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ALIEN INVASION")
        pygame.display.update()
        self.ship = Ship(self)
    def run_game(self):
        '''
        open = True
        while open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    open = False
        pygame.quit()
        '''
        
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    def _check_events(self):
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(event)
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__=="__main__":
    #Make a new game instance, start a game:
    ai = AlienInvasion()
    ai.run_game()