# -*- coding:utf-8 -*-

import sys
import pygame

from Player import Player
from Scene import *
from Settings import *
from PopUpBox import *
from Battle import *
from Monster import *

class GameManager:
    def __init__(self):
        self.window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height)) #初始化窗口
        self.title = pygame.display.set_caption(WindowSettings.name) #初始化标题
        self.clock = pygame.time.Clock()
        self.player = Player(WindowSettings.width // 2, WindowSettings.height // 2)
        self.state = GameState(1) #设置初始状态为主界面
        self.scene = MainMenu(self.window)

    def game_reset(self):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Necessary game components here ↓
    def tick(self, fps):
        self.clock.tick(fps)

    def get_time(self):
        return self.clock.get_time()

    # Scene-related update functions here ↓
    def flush_scene(self, GOTO:SceneType):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update(self):
        self.tick(30)
        if self.state == GameState.MAIN_MENU:
            self.update_main_menu(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_WILD:
            self.update_wild(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_CASTLE:
            self.update_castle(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_TEMPLE:
            self.update_temple(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_HUT:
            self.update_hut(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_BATTLE:
            self.update_battle(pygame.event.get())
        elif self.state == GameState.GAME_PLAY_BOSS:
            self.update_boss(pygame.event.get())

    def update_main_menu(self, events):
        for event in events:
            if event.type == pygame.QUIT: #点击退出
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #按下键盘按键
                #下方为开发时用主界面，正式版将改动
                if event.key == pygame.K_1:
                    self.scene = WildScene(self.window)
                    self.state = GameState.GAME_PLAY_WILD
                    self.scene.gen_WILD()
                elif event.key == pygame.K_2:
                    self.state = GameState.GAME_PLAY_CASTLE
                elif event.key == pygame.K_3:
                    self.state = GameState.GAME_PLAY_TEMPLE
                elif event.key == pygame.K_4:
                    self.state = GameState.GAME_PLAY_HUT
                elif event.key == pygame.K_5:
                    self.scene = MonsterBattle(self.window, self.player, Monster(0,0))
                    self.state = GameState.GAME_PLAY_BATTLE
                elif event.key == pygame.K_6:
                    self.state =GameState.GAME_PLAY_BOSS

    def update_wild(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.player.try_move(pygame.key.get_pressed(), self.scene.maxX, self.scene.maxY) #尝试移动
        
        # Then deal with regular updates
        self.player.update(0, 0)

    def update_castle(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_temple(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_hut(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_battle(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if self.scene.ATB == 300 and not self.scene.iscommanding:
                        self.scene.iscommanding = True #开启Command面板
                elif event.key == pygame.K_q:
                    if self.scene.iscommanding and not self.scene.ismagic:
                        self.scene.iscommanding = False #关闭Command面板
                    elif self.scene.iscommanding and self.scene.ismagic:
                        self.scene.ismagic = False #关闭Magic面板
                elif event.key == pygame.K_f:
                    if self.scene.iscommanding and not self.scene.ismagic:
                        self.scene.Attack() #Attack
                        self.scene.iscommanding = False
                elif event.key == pygame.K_r:
                    if self.scene.iscommanding and not self.scene.ismagic:
                        self.scene.ismagic = True #开启Magic面板
                elif event.key == pygame.K_z:
                    if self.scene.iscommanding and self.scene.ismagic:
                        self.scene.MagicFire() #使用Fire魔法
                        self.scene.ismagic = False
                        self.scene.iscommanding = False
                elif event.key == pygame.K_x:
                    if self.scene.iscommanding and self.scene.ismagic:
                        self.scene.MagicThunder() #使用Thunder魔法
                        self.scene.ismagic = False
                        self.scene.iscommanding = False

        # Then deal with regular updates
        self.scene.ATBmanage() #管理ATB

    def update_boss(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Then deal with regular updates
        pass

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
            self.render_main_menu()
        if self.state == GameState.GAME_PLAY_WILD:
            self.render_wild()
        if self.state == GameState.GAME_PLAY_BATTLE:
            self.render_battle()
        self.window.blit(pygame.font.Font(None, 36).render(f"{self.clock.get_fps()}", True, (255, 255, 255)), (0, 0))
        self.window.blit(pygame.font.Font(None, 36).render(f"{self.clock.get_rawtime()}", True, (255, 255, 255)), (0, 36))
    
    def render_main_menu(self):
        self.scene.render() #渲染主界面
    
    def render_wild(self):
        self.scene.update_camera(self.player) #更新Camera位置
        self.scene.render(self.player) #渲染野外场景

    def render_battle(self):
        self.scene.render() #渲染战斗场景

    def render_boss(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####