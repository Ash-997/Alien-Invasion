import pygame
from pygame.sprite import Sprite

class Boat(Sprite):
    def __init__(self,screen):
        super(Boat, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("image\shipshow.bmp")
        self.rect = self.image.get_rect()

