# -*- coding:utf-8 -*-

import pygame
from random import randint, random

from enum import Enum
from Settings import *
from NPCs import *
from PopUpBox import *
from Portal import *
from BgmPlayer import *
from Tile import *

class Scene():
    def __init__(self, window):
        self.image = None
        self.window = window
        self.image = None
        self.maxX = 0
        self.maxY = 0
        self.cameraX = 0
        self.cameraY = 0

    def trigger_dialog(self, npc):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_dialog(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_battle(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def trigger_shop(self, npc, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_shop(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_camera(self, player):
        #设置Camera位置
        if player.x < WindowSettings.width // 2:
            self.cameraX = 0
        elif player.x > self.maxX - WindowSettings.width // 2:
            self.cameraX = self.maxX - WindowSettings.width
        else:
            self.cameraX = player.x - WindowSettings.width // 2
        if player.y < WindowSettings.height // 2:
            self.cameraY = 0
        elif player.y > self.maxY - WindowSettings.height // 2:
            self.cameraY = self.maxY - WindowSettings.height
        else:
            self.cameraY = player.y - WindowSettings.height // 2

    def render(self, player):
        player.draw(self.window, -self.cameraX, -self.cameraY)


class MainMenu():
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load(GamePath.menu)
        self.bg = pygame.transform.scale(self.bg, (WindowSettings.width, WindowSettings.height))
        self.font = pygame.font.Font(None, 36) #主界面文字大小
        self.text1 = self.font.render("Press 1 to enter wild scene", True, (0, 0, 0)) #主界面文字内容1
        self.textRect1 = self.text1.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 500)) #主界面文字位置1
        self.text2 = self.font.render("Press 2 to enter castle scene", True, (0, 0, 0)) #主界面文字内容2
        self.textRect2 = self.text2.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 450)) #主界面文字位置2
        self.text3 = self.font.render("Press 3 to enter temple scene", True, (0, 0, 0)) #主界面文字内容3
        self.textRect3 = self.text3.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 400)) #主界面文字位置3
        self.text4 = self.font.render("Press 4 to enter hut scene", True, (0, 0, 0)) #主界面文字内容4
        self.textRect4 = self.text4.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 350)) #主界面文字位置4
        self.text5 = self.font.render("Press 5 to enter battle scene", True, (0, 0, 0)) #主界面文字内容5
        self.textRect5 = self.text5.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 300)) #主界面文字位置5
        self.text6 = self.font.render("Press 6 to enter boss scene", True, (0, 0, 0)) #主界面文字内容6
        self.textRect6 = self.text6.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 250)) #主界面文字位置6

    def render(self):
        self.window.blit(self.bg, (0, 0))
        self.window.blit(self.text1, self.textRect1) #显示主界面文字1
        self.window.blit(self.text2, self.textRect2) #显示主界面文字2
        self.window.blit(self.text3, self.textRect3) #显示主界面文字3
        self.window.blit(self.text4, self.textRect4) #显示主界面文字4
        self.window.blit(self.text5, self.textRect5) #显示主界面文字5
        self.window.blit(self.text6, self.textRect6) #显示主界面文字6

class CityScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        
        self.gen_CITY()
        self.type = SceneType.CITY

    def gen_city_map(self):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def gen_city_obstacle(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_CITY(self):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


class WildScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        self.map = None
        self.obstacles = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.maxX = SceneSettings.tileXnum * SceneSettings.tileWidth
        self.maxY = SceneSettings.tileYnum * SceneSettings.tileHeight

    def gen_wild_map(self):
        self.map = Tile(pygame.image.load(GamePath.groundTiles))
        self.portals.add(Portal(1000, 1000, 0, 0))

    def gen_wild_obstacle(self):
        midx = 15
        midy = 8
        self.obstacles = pygame.sprite.Group()
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                if random() < 0.05 and not (i in range(midx - 3, midx + 3) and j in range (midy - 3, midy + 3)):
                    self.obstacles.add(Tile(pygame.image.load(GamePath.tree[randint(0,1)]), SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))

    def gen_WILD(self):
        self.gen_wild_map()
        self.gen_wild_obstacle()

    def gen_monsters(self, num = 10):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def render(self, player):
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.map.draw(self.window, SceneSettings.tileWidth * i - self.cameraX, SceneSettings.tileHeight * j - self.cameraY)
        for portal in self.portals:
            portal.draw(self.window, - self.cameraX, - self.cameraY)
        for img in self.obstacles:
            img.draw(self.window, - self.cameraX, - self.cameraY)
        return super().render(player)


class BossScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        self.gen_BOSS()
        self.type = SceneType.BOSS

    # Overwrite Scene's function
    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_boss_obstacle(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_boss_map(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_BOSS(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####