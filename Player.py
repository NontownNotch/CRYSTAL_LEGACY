# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        self.imagefront = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.playerfront]
        self.imageback = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.playerback]
        self.imageleft = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.playerleft]
        self.imageright = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.playerright]
        self.images = self.imagefront
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.move = [False, False, False, False]
        self.HP = PlayerSettings.playerHP
        self.MP = PlayerSettings.playerMP
        self.attack = PlayerSettings.playerAttack
        self.defence = PlayerSettings.playerDefence
        self.money = PlayerSettings.playerMoney
        self.battlestandimage = pygame.image.load(GamePath.playerbattlestandimage)
        self.battlemagicimages = [pygame.image.load(img) for img in GamePath.playerbattlemagicimage]
        self.battlemagicindex = 0
        self.battlemagicimage = self.battlemagicimages[self.battlemagicindex]
        self.battleattackimage = pygame.image.load(GamePath.playerbattleattackimage)
        self.battleusemagicimage = pygame.image.load(GamePath.playerbattleusemagicimage)

    def attr_update(self, addCoins = 0, addHP = 0, addMP = 0, addAttack = 0, addDefence = 0):
        if self.money + addCoins < 0:
            return
        self.money += addCoins
        self.HP += addHP
        self.MP += addMP
        self.attack += addAttack
        self.defence += addDefence

    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def try_move(self, events, maxX = WindowSettings.width, maxY = WindowSettings.height):
        self.dx = self.dy = 0
        #尝试移动
        if events[pygame.K_w] and self.y >=PlayerSettings.playerHeight // 2:
            self.dy -= PlayerSettings.playerSpeed
            self.move[0] = True
        if events[pygame.K_s] and self.y <= maxY - PlayerSettings.playerHeight //2:
            self.dy += PlayerSettings.playerSpeed
            self.move[1] = True
        if events[pygame.K_a] and self.x >=PlayerSettings.playerWidth // 2:
            self.dx -= PlayerSettings.playerSpeed
            self.move[2] = True
        if events[pygame.K_d] and self.x <= maxX - PlayerSettings.playerWidth // 2:
            self.dx += PlayerSettings.playerSpeed
            self.move[3] = True
        if events[pygame.K_SPACE]:
            self.dx = self.dx * 2
            self.dy = self.dy * 2
        self.x += self.dx
        self.y += self.dy

    def update(self, scene):
        #设置人物图像
        if self.move == [True, False, False, False] or self.move == [True, False, True, True]:
            self.index = (self.index + 1) % 12
            self.images = self.imageback
        elif self.move == [False, True, False, False] or self.move == [False, True, True, True]:
            self.index = (self.index + 1) % 12
            self.images = self.imagefront
        elif self.move == [False, False, True, False] or self.move == [True, False, True, False] or self.move == [False, True, True, False] or self.move == [True, True, True, False]:
            self.index = (self.index + 1) % 12
            self.images = self.imageleft
        elif self.move == [False, False, False, True] or self.move == [True, False, False, True] or self.move == [False, True, False, True] or self.move == [True, True, False, True]:
            self.index = (self.index + 1) % 12
            self.images = self.imageright
        else:
            self.index = 0
        self.image = self.images[self.index]
        self.move = [False, False, False, False]
        #设置人物位置
        self.rect.center = (self.x, self.y)
        if pygame.sprite.spritecollide(self, scene.obstacles, False):
            self.x -= self.dx
            self.y -= self.dy
        self.rect.center = (self.x, self.y)


    def draw(self, window, dx=0, dy=0):
        window.blit(self.image, self.rect.move(dx, dy))

    def battlemagic(self):
        self.battlemagicindex = (self.battlemagicindex + 1) % 12
        self.battlemagicimage = self.battlemagicimages[self.battlemagicindex]
        return self.battlemagicimage