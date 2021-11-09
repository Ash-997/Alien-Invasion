import pygame
class Setting:
    def __init__(self):
        self.screen_width  =1200
       # self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.screen_height = 800
        self.bg = pygame.image.load("image\sky.bmp")
        self.bg_color = (28,134,238)
        #self.bullet_speed_factor = 45
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()
        self.score_scale = 1.5

    def initialize_dynamic_setting(self):
     self.ship_speed_factor = 1.5
     self.bullet_speed_factor = 10
     self.alien_speed_factor = 1
     self.alien_point = 50

    def increase_speed(self):
     self.ship_speed_factor *= self.speedup_scale
     self.bullet_speed_factor *= self.speedup_scale
     self.alien_speed_factor *= self.speedup_scale
     self.alien_point = int(self.alien_point * self.score_scale)
     print(self.alien_point)