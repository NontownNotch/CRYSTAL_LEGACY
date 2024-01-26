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
        self.istalking = False
        self.obstacles = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.popupbox = None
    
    def trigger_dialog(self, npc):
        if npc.talkCD == 0:
            self.istalking = True
            self.popupbox = DialogBox(self.window, npc)
    
    def end_dialog(self):
        self.istalking = False
    
    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def end_battle(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def trigger_shop(self, npc, player):
        if npc.talkCD == 0:
            self.istalking = True
            self.popupbox = ShoppingBox(self.window, npc, player)
    
    def end_shop(self):
        self.istalking = False
    
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
        for npc in self.npcs:
            npc.draw(self.window, - self.cameraX, - self.cameraY)
        player.draw(self.window, - self.cameraX, - self.cameraY) #渲染人物
        if self.istalking:
            self.popupbox.draw()

class MainMenu():
    def __init__(self, window):
        self.window = window
        self.background = pygame.transform.scale(pygame.image.load(GamePath.menu), (WindowSettings.width, WindowSettings.height))
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
        self.window.blit(self.background, (0, 0))
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
        self.maxX = self.cameramaxX = SceneSettings.tileXnum * SceneSettings.tileWidth
        self.maxY = self.cameramaxY = SceneSettings.tileYnum * SceneSettings.tileHeight
    
    def gen_wild_map(self):
        self.map = Tile(pygame.image.load(GamePath.groundTiles)) #读取地面
        self.portal.add(Portal(SceneSettings.tileXnum * SceneSettings.tileWidth * 61 // 64, SceneSettings.tileYnum * SceneSettings.tileHeight // 2, 0))
        self.portal.add(Portal(SceneSettings.tileXnum * SceneSettings.tileWidth * 3 // 64, SceneSettings.tileYnum * SceneSettings.tileHeight // 2, 1))
        self.portal.add(Portal(SceneSettings.tileXnum * SceneSettings.tileWidth // 2, SceneSettings.tileYnum * SceneSettings.tileHeight * 27 // 32, 2))
    
    def gen_wild_obstacle(self):
        midx = SceneSettings.tileXnum // 2
        midy = SceneSettings.tileYnum // 2
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
        for portal in self.portal:
            portal.draw(self.window, - self.cameraX, - self.cameraY)
        for img in self.obstacles:
            img.draw(self.window, - self.cameraX, - self.cameraY)
        return super().render(player)

class CastleScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.image = pygame.transform.scale(pygame.image.load(GamePath.castlebackground), (WindowSettings.width, WindowSettings.height * 160 // 9))
        self.rect = self.image.get_rect()
        self.rect.top = (0)
        self.maxX = WindowSettings.width * 7 // 12
        self.maxY = WindowSettings.height * 28 // 3
        self.minX = WindowSettings.width * 5 // 12
        self.minY = WindowSettings.height * 232 // 27
        self.cameramaxX = WindowSettings.width
        self.cameramaxY = WindowSettings.height * 160 // 9
    
    def gen_castle_obstacle(self):
        for i in [
            (WindowSettings.width * 5 // 12, WindowSettings.height * 388 // 45),
            (WindowSettings.width * 5 // 12, WindowSettings.height * 1172 // 135),
            (WindowSettings.width * 5 // 12, WindowSettings.height * 1196 // 135),
            (WindowSettings.width * 5 // 12, WindowSettings.height * 1204 // 135),
            (WindowSettings.width * 5 // 12, WindowSettings.height * 404 // 45),
            (WindowSettings.width * 5 // 12, WindowSettings.height * 1244 // 135),
            (WindowSettings.width * 9 // 20, WindowSettings.height * 236 // 27),
            (WindowSettings.width * 9 // 20, WindowSettings.height * 1252 // 135),
            (WindowSettings.width * 31 // 60, WindowSettings.height * 236 // 27),
            (WindowSettings.width * 31 // 60, WindowSettings.height * 1252 // 135),
            (WindowSettings.width * 11 // 20, WindowSettings.height * 388 // 45),
            (WindowSettings.width * 11 // 20, WindowSettings.height * 1172 // 135),
            (WindowSettings.width * 11 // 20, WindowSettings.height * 1196 // 135),
            (WindowSettings.width * 11 // 20, WindowSettings.height * 1204 // 135),
            (WindowSettings.width * 11 // 20, WindowSettings.height * 404 // 45),
            (WindowSettings.width * 11 // 20, WindowSettings.height * 1244 // 135)
            ]:
            self.obstacles.add(Tile(pygame.image.load(GamePath.emptyobstacles), i[0], i[1]))
    
    def gen_castle(self):
        self.gen_castle_obstacle()
        self.npcs.add(Cid(960, 9312, "Cid", "Use your magic power to investigate the Crystal Temple."))
        self.portal.add(Portal(960, 10048, 3))
    
    def render(self, player):
        self.window.blit(self.image, self.rect.move(-self.cameraX, -self.cameraY))
        return super().render(player)

class TempleScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.image = pygame.transform.scale(pygame.image.load(GamePath.templebackground), (WindowSettings.width, WindowSettings.width * 10))
        self.rect = self.image.get_rect()
        self.rect.top = (0)
        self.maxX = 1376
        self.maxY = 10112
        self.minX = 544
        self.minY = 9280
        self.cameramaxX = WindowSettings.width
        self.cameramaxY = WindowSettings.width * 10
    
    def gen_temple_obstacle(self):
        for i in [
            (544, 9344),
            (544, 9984),
            (608, 9408),
            (608, 9984),
            (672, 9280),
            (672, 9984),
            (736, 9280),
            (736, 9568),
            (736, 9600),
            (736, 9984),
            (800, 9984),
            (1056, 9984),
            (1120, 9280),
            (1120, 9568),
            (1120, 9600),
            (1120, 9984),
            (1184, 9280),
            (1184, 9984),
            (1248, 9408),
            (1248, 9984),
            (1312, 9344),
            (1312, 9984)
            ]:
            self.obstacles.add(Tile(pygame.image.load(GamePath.emptyobstacles), i[0], i[1]))
    
    def gen_temple(self):
        self.gen_temple_obstacle()
        self.portal.add(Portal(960, 10080, 4))
    
    def render(self, player):
        self.window.blit(self.image, self.rect.move(-self.cameraX, -self.cameraY))
        return super().render(player)

class HutScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.image = pygame.transform.scale(pygame.image.load(GamePath.hutbackground), (WindowSettings.width, WindowSettings.width * 10))
        self.rect = self.image.get_rect()
        self.rect.top = (0)
        self.maxX = 1408
        self.maxY = 9984
        self.minX = 512
        self.minY = 9408
        self.cameramaxX = WindowSettings.width
        self.cameramaxY = WindowSettings.width * 10
    
    def gen_hut_obstacle(self):
        for i in [
            (512, 9408),
            (512, 9792),
            (544, 9568),
            (544, 9632),
            (576, 9856),
            (608, 9568),
            (608, 9632),
            (640, 9920),
            (768, 9568),
            (768, 9952),
            (832, 9536),
            (832, 9600),
            (832, 9952),
            (896, 9408),
            (896, 9568),
            (896, 9920),
            (960, 9408),
            (960, 9920),
            (1056, 9504),
            (1088, 9920),
            (1120, 9440),
            (1120, 9504),
            (1152, 9792),
            (1216, 9792),
            (1248, 9440),
            (1248, 9504),
            (1280, 9792),
            (1312, 9504),
            (1344, 9728)
            ]:
            self.obstacles.add(Tile(pygame.image.load(GamePath.emptyobstacles), i[0], i[1]))
    
    def gen_hut(self):
        self.gen_hut_obstacle()
        self.npcs.add(ShopNPC(1312, 9696, "Knight"))
        self.portal.add(Portal(1056, 9952, 3))
    
    def render(self, player):
        self.window.blit(self.image, self.rect.move(-self.cameraX, -self.cameraY))
        return super().render(player)