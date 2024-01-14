# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        self.x = x
        self.y = y
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

    def try_move(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update(self, width,height):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def battlemagic(self):
        self.battlemagicindex = (self.battlemagicindex + 1) % 12
        self.battlemagicimage = self.battlemagicimages[self.battlemagicindex]
        return self.battlemagicimage