from Settings import *

import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, index):
        super().__init__()
        self.images = GamePath.portal
        self.index = index
        self.image = pygame.transform.scale(pygame.image.load(self.images[self.index]), PortalSettings.size[self.index])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self, window, dx=0, dy=0):
        rect = self.rect
        rect = rect.move(dx, dy)
        window.blit(self.image, rect)