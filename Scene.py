# -*- coding:utf-8 -*-

import pygame
from random import randint, random

from enum import Enum
from Settings import *
#from NPCs import *
#from PopUpBox import *
#from Portal import *
#from BgmPlayer import *
#from Tile import *

class Scene():
    def __init__(self, window):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

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
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def render(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


class MainMenu():
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 36) #主界面文字大小
        self.text1 = self.font.render("Press 1 to enter ...scene", True, (255, 255, 255)) #主界面文字内容1
        self.textRect1 = self.text1.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 500)) #主界面文字位置1
        self.text2 = self.font.render("Press 2 to enter ...scene", True, (255, 255, 255)) #主界面文字内容2
        self.textRect2 = self.text2.get_rect(center=(WindowSettings.width // 2, WindowSettings.height - 400)) #主界面文字位置2

    def render(self):
        self.window.blit(self.text1, self.textRect1) #显示主界面文字1
        self.window.blit(self.text2, self.textRect2) #显示主界面文字2

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
        
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_wild_map(self):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_wild_obstacle(self):
        
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_WILD(self):
        
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_monsters(self, num = 10):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


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