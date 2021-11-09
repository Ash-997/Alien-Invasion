import pygame.font
from pygame.sprite import Group
from shiip import Ship
from boat import Boat


class Scoreboard():
    def __init__(self, ai_setting, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("None", 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        # score_str = str(self.stats.score)
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)

        self.score_image = self.font.render(score_str, True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        # lev = int(round(self.stats.level,-1))
        # lev_str = "{:,}".format(lev)
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_ships(self):
        #self.ships = Group()
        self.boats = Group()
        for ship_number in range(self.stats.ship_left):
            bat = Boat(self.screen)
            bat.rect.x = 10 + ship_number * bat.rect.width
            bat.rect.y = 10
            self.boats.add(bat)

          #ship = Ship(self.ai_setting,self.screen)
          #ship.rect.x = 10 + ship_number * ship.rect.width
          #ship.rect.y = 10
          #self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # self.screen.blit(self.kil,self.bil)
        #self.ships.draw(self.screen)
        self.boats.draw(self.screen)