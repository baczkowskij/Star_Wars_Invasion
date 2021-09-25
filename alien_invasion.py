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
        pygame.display.set_capton("ALIEN INVASION")
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

if __name__=="main":
    #Make a new game instance, start a game:
    ai = AlienInvasion()
    ai.run_game()