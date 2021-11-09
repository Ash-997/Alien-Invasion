import pygame
from setting import Setting
from game_stats import GameStats
from alien import Alien
from shiip import Ship
import game_fun as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard



def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    alien = Alien(ai_setting, screen)
    # screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_setting, screen)
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_setting, screen, ship, aliens)
    play_button = Button(ai_setting, screen, "Play")

    while True:
        gf.check_event(ai_setting,screen,stats,sb, play_button,ship,aliens,bullets)
        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            #bullets.update()
            gf.update_bullet(ai_setting, screen,stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_setting, stats,sb, screen, ship, aliens, bullets)
            gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets,play_button)


run_game()
