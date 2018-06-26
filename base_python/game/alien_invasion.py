import pygame
from setting import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_setting = Settings()
    #bg_color = (50, 50 , 50)
    #screen = pygame.display.set_mode((1200, 800))
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    #pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_setting)

    bullets = Group()
    print("Total initliasize bullet: {0}".format(len(bullets)))
    #bullet = Bullet(ai_setting, screen, ship)
    pygame.display.set_caption(ai_setting.caption)

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_setting, screen, ship, bullets)

run_game()
