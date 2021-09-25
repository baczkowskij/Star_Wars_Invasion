#setting up a game environemnt for Alien Invasion:
#importing system functions:
import sys
#importing pygame:
import pygame
#importing a settings module:
from settings import Settings

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(event)
                    sys.exit()
                self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__=="__main__":
    #Make a new game instance, start a game:
    ai = AlienInvasion()
    ai.run_game()