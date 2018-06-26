import sys
import pygame
from bullet import Bullet

def event_keyup(event, ship):
   if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            ship.left_move = False
        elif event.key == pygame.K_RIGHT:
            ship.right_move = False
        elif event.key == pygame.K_UP:
            ship.up_move = False
        elif event.key == pygame.K_DOWN:
            ship.down_move = False

def event_keydown(event, ai_setting, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.right_move = True
        elif event.key == pygame.K_LEFT:
            ship.left_move = True
        elif event.key == pygame.K_SPACE:
            fire_bullets(ai_setting, screen, ship, bullets)
        elif event.key == pygame.K_UP:
            ship.up_move = True
        elif event.key == pygame.K_DOWN:
            ship.down_move = True

def check_events(ai_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.key == pygame.K_q:
            sys.exit()

        event_keyup(event, ship)
        event_keydown(event, ai_setting, screen, ship, bullets)

def fire_bullets(ai_setting, screen, ship, bullets):
        if len(bullets) < 3:
            new_bullet = Bullet(ai_setting, screen, ship)
            bullets.add(new_bullet)

def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_setting, screen, ship, bullets):
    screen.fill(ai_setting.bg_color)
    # draw the bullets on screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    update_bullets(bullets)
    ship.blitme()
    pygame.display.flip()
