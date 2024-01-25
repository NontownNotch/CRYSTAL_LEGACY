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
        self.window = window
        self.maxX = self.cameramaxX = 0
        self.maxY = self.cameramaxY = 0
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
        if player.x < WindowSettings.width // 2: #如果人物距左侧边框小于窗口大小一半
            self.cameraX = 0
        elif player.x > self.cameramaxX - WindowSettings.width // 2: #如果人物距上侧边框小于窗口大小一半
            self.cameraX = self.cameramaxX - WindowSettings.width
        else:
            self.cameraX = player.x - WindowSettings.width // 2
        if player.y < WindowSettings.height // 2: #如果人物距上侧边框小于窗口大小一半
            self.cameraY = 0
        elif player.y > self.cameramaxY - WindowSettings.height // 2: #如果人物距下侧边框小于窗口大小一半
            self.cameraY = self.cameramaxY - WindowSettings.height
        else:
            self.cameraY = player.y - WindowSettings.height // 2

    def render(self, player):
        player.draw(self.window, -self.cameraX, -self.cameraY) #渲染人物


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

class WildScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        self.map = None
        self.obstacles = pygame.sprite.Group()
        self.castleportal = pygame.sprite.Group()
        self.templeportal = pygame.sprite.Group()
        self.hutportal = pygame.sprite.Group()
        self.maxX = self.cameramaxX = SceneSettings.tileXnum * SceneSettings.tileWidth
        self.maxY = self.cameramaxY = SceneSettings.tileYnum * SceneSettings.tileHeight

    def gen_wild_map(self):
        self.map = Tile(pygame.image.load(GamePath.groundTiles)) #读取地面
        self.castleportal.add(Portal(3904, 2048, 0))
        self.templeportal.add(Portal(192, 2048, 1))
        self.hutportal.add(Portal(2048, 3456, 2))

    def gen_wild_obstacle(self):
        midx = 32
        midy = 32
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                if random() < 0.05 and (not i in range(midx - 3, midx + 3) and not j in range (midy - 3, midy + 3)):
                    self.obstacles.add(Tile(pygame.image.load(GamePath.tree[randint(0,1)]), SceneSettings.tileWidth * i, SceneSettings.tileHeight * j)) #在(i * tile width, j * tile height)处添加障碍物

    def gen_WILD(self):
        self.gen_wild_map()
        self.gen_wild_obstacle()

    def gen_monsters(self, num = 10):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def render(self, player):
        #偏移(- cameraX, - cameraY)
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.map.draw(self.window, SceneSettings.tileWidth * i - self.cameraX, SceneSettings.tileHeight * j - self.cameraY) #绘制地面
        for portal in self.castleportal:
            portal.draw(self.window, - self.cameraX, - self.cameraY)
        for portal in self.templeportal:
            portal.draw(self.window, - self.cameraX, - self.cameraY)
        for portal in self.hutportal:
            portal.draw(self.window, - self.cameraX, - self.cameraY)
        for img in self.obstacles:
            img.draw(self.window, - self.cameraX, - self.cameraY)
        return super().render(player)

class CastleScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.image = pygame.transform.scale(pygame.image.load(GamePath.castlebackground), (WindowSettings.width, WindowSettings.width * 10))
        self.rect = self.image.get_rect()
        self.rect.top = (0)
        self.maxX = 1120
        self.maxY = 10080
        self.minX = 800
        self.minY = 9280
        self.cameramaxX = WindowSettings.width
        self.cameramaxY = WindowSettings.width * 10
        self.obstacles = pygame.sprite.Group()
    
    def gen_castle_obstacle(self):
        for i in [(864, 10016), (800, 9952), (800, 9760), (800, 9696), (800, 9632), (800, 9568), (864, 9504), (864, 9440), (800, 9376), (800, 9312), (992, 10016), (1056, 9952), (1056, 9760), (1056, 9696), (1056, 9632), (1056, 9568), (992, 9504), (992, 9440), (1056, 9376), (1056, 9312)]:
            self.obstacles.add(Tile(pygame.image.load(GamePath.emptyobstacles), i[0], i[1]))
    
    def render(self, player):
        self.window.blit(self.image, self.rect.move(-self.cameraX, -self.cameraY))
        return super().render(player)