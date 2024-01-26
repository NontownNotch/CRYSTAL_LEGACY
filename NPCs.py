import pygame

from Settings import *
from Attributes import *

class NPC(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y, name):
        # Initialize father classes
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.talkCD = 0
    
    def update(self):
        raise NotImplementedError
    
    def draw(self, window, dx=0, dy=0):
        window.blit(self.image, self.rect.move(dx, dy))

class Cid(NPC):
    def __init__(self, x, y, name, dialog):
        super().__init__(x, y, name)
        self.image = pygame.transform.scale(pygame.image.load(GamePath.cid), (NPCSettings.npcWidth, NPCSettings.npcHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dialog = dialog
    
    def update(self):
        if self.talkCD != 0:
            self.talkCD -=1

class ShopNPC(NPC):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.image = pygame.transform.scale(pygame.image.load(GamePath.knight), (NPCSettings.npcWidth, NPCSettings.npcHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        if self.talkCD != 0:
            self.talkCD -=1