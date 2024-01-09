# -*- coding:utf-8 -*-

import sys
import pygame

#from Player import Player
from Scene import *
from Settings import *
#from PopUpBox import *

class GameManager:
    def __init__(self):
        self.window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height)) #初始化窗口
        self.title = pygame.display.set_caption(WindowSettings.name) #初始化标题
        self.clock = pygame.time.Clock()
        self.state = GameState(1) #设置初始状态为主界面

    def game_reset(self):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Necessary game components here ↓
    def tick(self, fps):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def get_time(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Scene-related update functions here ↓
    def flush_scene(self, GOTO:SceneType):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update(self):
        self.clock.tick(30)
        if self.state == GameState.MAIN_MENU:
            self.update_main_menu(pygame.event.get()) #执行self.update_main_menu()函数，pygame.event.get()返回为List

    def update_main_menu(self, events):
        for event in events:
            if event.type == pygame.QUIT: #点击退出
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #按下键盘按键
                #下方为开发时用主界面，正式版将改动
                pass #功能待定

    def update_city(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_wild(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
        
        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_boss(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
        
        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Collision-relate update funtions here ↓
    def update_collide(self):
        # Player -> Obstacles
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Player -> NPCs; if multiple NPCs collided, only first is accepted and dealt with.
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Player -> Monsters
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
        
        # Player -> Portals
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
        
        # Player -> Boss
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_NPCs(self):
        # This is not necessary. If you want to re-use your code you can realize this.
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Render-relate update functions here ↓
    def render(self):
        if self.state == GameState.MAIN_MENU:
            self.render_main_menu() #执行self.render_main_menu()函数
    
    def render_main_menu(self):
        MainMenu(self.window).render()
    
    def render_city(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def render_wild(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def render_boss(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

