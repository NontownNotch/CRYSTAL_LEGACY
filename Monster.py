import pygame

from Settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, HP = 10, Attack = 3, Money = 15, range = 128):
        super().__init__()
        self.name = "Sweeper"
        self.image = pygame.transform.scale(pygame.image.load(GamePath.monster), (MonsterSettings.monsterWidth, MonsterSettings.monsterHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.skillname = "Machine Gun"
        self.x = self.initialX = x
        self.y = y
        self.speed = MonsterSettings.monsterSpeed
        self.direction = 1
        self.patrollingRange = range
        self.HP = HP
        self.attack = Attack
        self.money = Money
    
    def update(self):
        self.x += self.speed * self.direction
        if abs(self.x - self.initialX) > self.patrollingRange:
            self.direction *= -1  # 反转方向
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.center = (self.x, self.y)

    def attr_update(self, HP):
        self.HP += HP
    
    def draw(self, window, dx=0, dy=0):
        window.blit(self.image, self.rect.move(dx, dy))

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.name = "Bahamut"
        self.image = pygame.transform.scale(pygame.image.load(GamePath.boss), (256, 210))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.skillname = "Megaflare"
        self.x = x
        self.y = y
        self.HP = 9999
        self.attack = 50
        self.money = 0
    
    def attr_update(self, HP):
        self.HP += HP
    
    def draw(self, window, dx=0, dy=0):
        window.blit(self.image, self.rect.move(dx, dy))