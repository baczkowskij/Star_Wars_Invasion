#setting up a game environemnt for Alien Invasion:
#importing system functions:
import sys
#importing pygame:
import pygame
#importing a settings module:
from settings import Settings
#importing a ship:
from ship import Ship
#importing an alien:
from alien import Alien
#importing a bullet
from bullet import Bullet

#class for Game Management:
class AlienInvasion:
    """All things concerning game assets and behaviour."""
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("ALIEN INVASION")
        pygame.display.update()
        self.ship = Ship(self)
        #list with an extra functionality:
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        '''x
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
            self._update_bullets()
            self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if (len(self.bullets)<self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
                if bullet.rect.y<=0:
                    self.bullets.remove(bullet)
        collisions = pygame.sprite.pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        alien=Alien(self)
        alien_width, alien_height = alien.rect.size
        #determinig the number of colimns:
        available_x_space = self.settings.screen_width - (2*alien_width)
        numebr_of_aliens_x = available_x_space // (2*alien_width)
        #determinig the number of rows:
        ship_height=self.ship.rect.height
        available_y_space = self.settings.screen_height - (4*alien_height)-ship_height
        numebr_of_aliens_y = available_y_space // (2*alien_height)
        for row_number in range(numebr_of_aliens_y):
            for alien_number in range(numebr_of_aliens_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self,alien_number,row_number):
        new_alien = Alien(self)
        alien_width = new_alien.rect.width
        alien_height = new_alien.rect.height
        #alien x position:
        new_alien.x = alien_width +2*alien_width*alien_number
        new_alien.rect.x=new_alien.x
        #alien y position
        new_alien.y = alien_height + 2*alien_height*row_number
        new_alien.rect.y=new_alien.y
        self.aliens.add(new_alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *=-1
    
if __name__=="__main__":
    #Make a new game instance, start a game:
    ai = AlienInvasion()
    ai.run_game()