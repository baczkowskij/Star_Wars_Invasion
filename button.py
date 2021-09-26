import pygame.font
class Button:
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width,self.height = 200,50
        self.button_color = (255,255,255)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self._prep_message(msg)

    def _prep_message(self, msg):
        self.msg_img = self.font.render(msg,True, self.text_color,self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center=self.screen_rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_img,self.msg_img_rect)