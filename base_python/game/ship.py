import pygame
from bullet import Bullet

class Ship():
    def __init__(self, screen, ai_setting):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.ai_setting = ai_setting

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.right_move and self.rect.centerx < self.screen_rect.right - 25:
            self.rect.centerx += self.ai_setting.ship_speed_factor
            print("K_R:{0}, act:{1}".format(self.screen_rect.right, self.rect.centerx))

        if self.left_move and self.rect.centerx > self.screen_rect.left + 25:
            self.rect.centerx -= self.ai_setting.ship_speed_factor
            print("K_L:{0}, act:{1}".format(self.screen_rect.left, self.rect.centerx))

        if self.up_move and self.rect.bottom > 50:
            self.rect.bottom -= self.ai_setting.ship_speed_factor
            print("K_U:{0}, act:{1}".format(0, self.rect.bottom))

        if self.down_move and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ai_setting.ship_speed_factor
            print("K_D:{0}, act:{1}".format(self.screen_rect.bottom, self.rect.bottom))
