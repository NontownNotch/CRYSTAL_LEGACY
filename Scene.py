import pygame
from random import randint, random

from enum import Enum
from Settings import *
from NPCs import *
from Monster import *
from Battle import *
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
        self.monsters = pygame.sprite.Group()
        self.popupbox = None
    
    def trigger_dialog(self, npc):
        if npc.talkCD == 0:
            self.istalking = True
            self.popupbox = DialogBox(self.window, npc)
    
    def end_dialog(self):
        self.istalking = False
    
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
        for monster in self.monsters:
            monster.draw(self.window, - self.cameraX, - self.cameraY)
        for npc in self.npcs:
            npc.draw(self.window, - self.cameraX, - self.cameraY)
        player.draw(self.window, - self.cameraX, - self.cameraY) #渲染人物
        if self.istalking:
            self.popupbox.draw()

class MainMenu():
    def __init__(self, window):
        self.window = window
        self.background = pygame.transform.scale(pygame.image.load(GamePath.menu), (WindowSettings.width, WindowSettings.height))
        self.font = pygame.font.Font(None, int(pow(WindowSettings.width * WindowSettings.height, 0.5) // 30)) #主界面文字大小
        self.text1 = self.font.render("PRESS ANY BUTTON", True, (0, 0, 0)) #主界面文字内容1
        self.textRect1 = self.text1.get_rect(center=(WindowSettings.width // 2, WindowSettings.height * 3 // 4)) #主界面文字位置1
    
    def render(self):
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.text1, self.textRect1) #显示主界面文字1

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
        self.gen_monsters()
    
    def gen_monsters(self, num = 10):
        while num > 0:
            self.monsters.add(Monster(randint(WindowSettings.width // 30, WindowSettings.width * 29 // 15), randint(WindowSettings.height * 8 // 135, WindowSettings.height * 56 // 15), 1000, 25, 15, randint(WindowSettings.width // 15, WindowSettings.width // 6)))
            num -= 1
    
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
        self.npcs.add(Cid(WindowSettings.width // 2, WindowSettings.height * 388 // 45, "Cid", "Use your magic power to investigate the Crystal Temple."))
        self.portal.add(Portal(WindowSettings.width // 2, WindowSettings.height * 1256 // 135, 3))
    
    def render(self, player):
        self.window.blit(self.image, self.rect.move(-self.cameraX, -self.cameraY))
        return super().render(player)

class TempleScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.image = pygame.transform.scale(pygame.image.load(GamePath.templebackground), (WindowSettings.width, WindowSettings.height * 160 // 9))
        self.rect = self.image.get_rect()
        self.rect.top = (0)
        self.maxX = WindowSettings.width * 43 // 60
        self.maxY = WindowSettings.height * 1264 // 135
        self.minX = WindowSettings.width * 17 // 60
        self.minY = WindowSettings.height * 232 // 27
        self.cameramaxX = WindowSettings.width
        self.cameramaxY = WindowSettings.width * 10
    
    def gen_temple_obstacle(self):
        for i in [
            (WindowSettings.width * 17 // 60, WindowSettings.height * 1168 // 135),
            (WindowSettings.width * 17 // 60, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 19 // 60, WindowSettings.height * 392 // 45),
            (WindowSettings.width * 19 // 60, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 7 // 20, WindowSettings.height * 232 // 27),
            (WindowSettings.width * 7 // 20, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 23 // 60, WindowSettings.height * 232 // 27),
            (WindowSettings.width * 23 // 60, WindowSettings.height * 1196 // 135),
            (WindowSettings.width * 23 // 60, WindowSettings.height * 80 // 9),
            (WindowSettings.width * 23 // 60, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 5 // 12, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 11 // 20, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 7 // 12, WindowSettings.height * 232 // 27),
            (WindowSettings.width * 7 // 12, WindowSettings.height * 1196 // 135),
            (WindowSettings.width * 7 // 12, WindowSettings.height * 80 // 9),
            (WindowSettings.width * 7 // 12, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 37 // 60, WindowSettings.height * 232 // 27),
            (WindowSettings.width * 37 // 60, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 13 // 20, WindowSettings.height * 392 // 45),
            (WindowSettings.width * 13 // 20, WindowSettings.height * 416 // 45),
            (WindowSettings.width * 41 // 60, WindowSettings.height * 1168 // 135),
            (WindowSettings.width * 41 // 60, WindowSettings.height * 416 // 45)
            ]:
            self.obstacles.add(Tile(pygame.image.load(GamePath.emptyobstacles), i[0], i[1]))
    
    def gen_temple(self):
        self.gen_temple_obstacle()
        self.portal.add(Portal(WindowSettings.width // 2, WindowSettings.height * 28 // 3, 4))
        self.monsters.add(Boss(WindowSettings.width // 2, WindowSettings.height * 232 // 27))
    
    def render(self, player):
        self.window.blit(self.image, self.rect.move(-self.cameraX, -self.cameraY))
        return super().render(player)

class HutScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.image = pygame.transform.scale(pygame.image.load(GamePath.hutbackground), (WindowSettings.width, WindowSettings.width * 10))
        self.rect = self.image.get_rect()
        self.rect.top = (0)
        self.maxX = WindowSettings.width * 11 // 15
        self.maxY = WindowSettings.height * 416 // 45
        self.minX = WindowSettings.width * 4 // 15
        self.minY = WindowSettings.height * 392 // 45
        self.cameramaxX = WindowSettings.width
        self.cameramaxY = WindowSettings.width * 10
    
    def gen_hut_obstacle(self):
        for i in [
            (WindowSettings.width * 4 // 15, WindowSettings.height * 392 // 45),
            (WindowSettings.width * 4 // 15, WindowSettings.height * 136 // 15),
            (WindowSettings.width * 17 // 60, WindowSettings.height * 1196 // 135),
            (WindowSettings.width * 17 // 60, WindowSettings.height * 1204 // 135),
            (WindowSettings.width * 3 // 10, WindowSettings.height * 1232 // 135),
            (WindowSettings.width * 19 // 60, WindowSettings.height * 1196 // 135),
            (WindowSettings.width * 19 // 60, WindowSettings.height * 1204 // 135),
            (WindowSettings.width // 3, WindowSettings.height * 248 // 27),
            (WindowSettings.width * 2 // 5, WindowSettings.height * 1196 // 135),
            (WindowSettings.width * 2 // 5, WindowSettings.height * 1244 // 135),
            (WindowSettings.width * 13 // 30, WindowSettings.height * 1192 // 135),
            (WindowSettings.width * 13 // 30, WindowSettings.height * 80 // 9),
            (WindowSettings.width * 13 // 30, WindowSettings.height * 1244 // 135),
            (WindowSettings.width * 7 // 15, WindowSettings.height * 392 // 45),
            (WindowSettings.width * 7 // 15, WindowSettings.height * 1196 // 135),
            (WindowSettings.width * 7 // 15, WindowSettings.height * 248 // 27),
            (WindowSettings.width // 2, WindowSettings.height * 392 // 45),
            (WindowSettings.width // 2, WindowSettings.height * 248 // 27),
            (WindowSettings.width * 11 // 20, WindowSettings.height * 44 // 5),
            (WindowSettings.width * 17 // 30, WindowSettings.height * 248 // 27),
            (WindowSettings.width * 7 // 12, WindowSettings.height * 236 // 27),
            (WindowSettings.width * 7 // 12, WindowSettings.height * 44 // 5),
            (WindowSettings.width * 3 // 5, WindowSettings.height * 136 // 15),
            (WindowSettings.width * 19 // 30, WindowSettings.height * 136 // 15),
            (WindowSettings.width * 13 // 20, WindowSettings.height * 236 // 27),
            (WindowSettings.width * 13 // 20, WindowSettings.height * 44 // 5),
            (WindowSettings.width * 2 // 3, WindowSettings.height * 136 // 15),
            (WindowSettings.width * 41 // 60, WindowSettings.height * 44 // 5),
            (WindowSettings.width * 7 // 10, WindowSettings.height * 1216 // 135)
            ]:
            self.obstacles.add(Tile(pygame.image.load(GamePath.emptyobstacles), i[0], i[1]))
    
    def gen_hut(self):
        self.gen_hut_obstacle()
        self.npcs.add(ShopNPC(WindowSettings.width * 41 // 60, WindowSettings.height * 404 // 45, "Knight"))
        self.portal.add(Portal(WindowSettings.width * 11 // 20, WindowSettings.height * 1244 // 135, 3))
    
    def render(self, player):
        self.window.blit(self.image, self.rect.move(-self.cameraX, -self.cameraY))
        return super().render(player)