import pygame
from typing import *
from Settings import *
from Monster import *
from Player import *

class Battle:
    def __init__(self, window, player, monster, fontSize: int = BattleSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255)) :
        self.window = window
        self.player = player
        self.monster = monster
        self.iscommanding = False #检测是否在Command状态
        self.ismagic = False #检测是否在Magic状态
        self.battlestatus = pygame.transform.scale(pygame.image.load(GamePath.battlestatus), (WindowSettings.width, WindowSettings.height // 5)) #设置战斗UI
        self.commandbackground = pygame.transform.scale(pygame.image.load(GamePath.commandbackground), (WindowSettings.width // 8 * 3, WindowSettings.height // 5)) #设置Command与Magic面板UI
        self.ATBbackground = pygame.transform.scale(pygame.image.load(GamePath.ATBbackground), (WindowSettings.width // 15, WindowSettings.height // 50)) #设置ATB条背景
        self.font = pygame.font.Font(None, fontSize)
        self.monstername = self.font.render(f"{self.monster.name}", True, fontColor)
        self.playername = self.font.render("Sansan", True, fontColor)
        self.HP = self.font.render(f"HP {self.player.HP} / {PlayerSettings.playerHP}", True, fontColor)
        self.MP = self.font.render(f"MP {self.player.MP} / {PlayerSettings.playerMP}", True, fontColor)
        self.CommandText = self.font.render("[E] Command", True, fontColor)
        self.CancelText = self.font.render("[Q] Cancel", True, fontColor)
        self.AttackText = self.font.render("[F] Attack", True, fontColor)
        self.MagicText = self.font.render("[R] Magic", True, fontColor)
        self.FireText = self.font.render("[Z] Fire", True, fontColor)
        self.ThunderText = self.font.render("[X] Thunder", True, fontColor)

    def render(self):
        self.window.blit(self.battlestatus, (BattleSettings.statusStartX, BattleSettings.statusStartY)) #显示战斗UI
        self.window.blit(self.monstername, (BattleSettings.textMonsterStartX, BattleSettings.textStartY)) #显示怪物名称
        self.window.blit(self.playername, (BattleSettings.textPlayerStartX, BattleSettings.textStartY)) #显示玩家名称
        self.window.blit(self.HP, (BattleSettings.textPlayerStatusStartX, BattleSettings.textStartY)) #显示玩家HP
        self.window.blit(self.MP, (BattleSettings.textPlayerStatusStartX, BattleSettings.textStartY + BattleSettings.textVerticalDist)) #显示玩家MP
        self.window.blit(self.ATBbackground, (BattleSettings.ATBStartX, BattleSettings.textStartY)) #显示玩家ATB条背景
        if not self.iscommanding:
            self.window.blit(self.CommandText, (BattleSettings.ATBStartX, BattleSettings.textStartY + BattleSettings.textVerticalDist)) #显示Command按键指引
        elif self.iscommanding:
            self.window.blit(self.commandbackground, (BattleSettings.statusStartX, BattleSettings.statusStartY)) #显示Command面板UI
            self.window.blit(self.CancelText, (BattleSettings.ATBStartX, BattleSettings.textStartY + BattleSettings.textVerticalDist)) #显示Cancel按键指引
            self.window.blit(self.AttackText, (BattleSettings.textMonsterStartX, BattleSettings.textStartY)) #显示Attack按键指引
            self.window.blit(self.MagicText, (BattleSettings.textMonsterStartX, BattleSettings.textStartY + BattleSettings.textVerticalDist)) #显示Magic按键指引
            if self.ismagic:
                self.window.blit(self.commandbackground, (BattleSettings.statusStartX, BattleSettings.statusStartY)) #显示Magic面板UI
                self.window.blit(self.FireText, (BattleSettings.textMonsterStartX, BattleSettings.textStartY)) #显示Fire魔法按键指引
                self.window.blit(self.ThunderText, (BattleSettings.textMonsterStartX, BattleSettings.textStartY + BattleSettings.textVerticalDist)) #显示Thunder魔法按键指引

class MonsterBattle(Battle):
    def __init__(self, window, player, monster):
        super().__init__(window, player, monster)
        self.background = pygame.transform.scale(pygame.image.load(GamePath.battlebackground), (WindowSettings.width, WindowSettings.height))
    
    def render(self):
        self.window.blit(self.background,(BattleSettings.boxStartX, BattleSettings.boxStartY)) #显示战斗背景
        return super().render()

class BossBattle(Battle):
    def __init__(self) -> None:
        super().__init__()