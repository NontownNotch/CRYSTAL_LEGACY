import pygame
from typing import *
from Settings import *
from Monster import *
from Player import *

class Battle:
    def __init__(self, window, player, monster, fontSize: int = BattleSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 0), bgColor: Tuple[int, int, int, int] = (0, 0, 0, 200)) :
        self.window = window
        self.player = player
        self.monster = monster
        self.battlestatus = pygame.transform.scale(pygame.image.load(GamePath.battlestatus), (WindowSettings.width, WindowSettings.height // 5))
        self.font = pygame.font.Font(None, fontSize)
        self.playername = self.font.render("Sansan", True, fontColor)
        self.HP = self.font.render(f"HP {self.player.HP} / {PlayerSettings.playerHP}", True, fontColor)
        self.MP = self.font.render(f"MP {self.player.MP} / {PlayerSettings.playerMP}", True, fontColor)

    def draw(self):
        self.window.blit(self.battlestatus, (BattleSettings.statusStartX, BattleSettings.statusStartY))
        self.window.blit(self.playername, (BattleSettings.textPlayerStartX, BattleSettings.textStartY))
        self.window.blit(self.HP, (BattleSettings.textPlayerStatusStartX, BattleSettings.textStartY))
        self.window.blit(self.MP, (BattleSettings.textPlayerStatusStartX, BattleSettings.textStartY + BattleSettings.textVerticalDist))

class MonsterBattle(Battle):
    def __init__(self, window, player, monster):
        super().__init__(window, player, monster)
        self.background = pygame.transform.scale(pygame.image.load(GamePath.battlebackground), (WindowSettings.width, WindowSettings.height))
    
    def draw(self):
        self.window.blit(self.background,(BattleSettings.boxStartX, BattleSettings.boxStartY))
        return super().draw()

class BossBattle(Battle):
    def __init__(self) -> None:
        super().__init__()