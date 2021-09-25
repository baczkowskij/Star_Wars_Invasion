#setting up a game environemnt for Alien Invasion:
#importing system functions:
import sys
#importing pygame:
import pygame

#class for Game Management:
class AlienInvasion:
    """All things concerning game assets and behaviour."""
    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
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
            pygame.display.flip()

if __name__=="__main__":
    #Make a new game instance, start a game:
    ai = AlienInvasion()
    ai.run_game()