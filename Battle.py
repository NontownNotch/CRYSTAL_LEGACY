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
        self.font = pygame.font.Font(None, fontSize)
        self.text = self.font.render("LLLLLLLLLLLLLLLLLLLLLLL", True, fontColor)
        self.textrect = self.text.get_rect(center = (BattleSettings.textStartX,BattleSettings.textStartY))

    def draw(self):
        self.window.blit(self.text, self.textrect)

class MonsterBattle(Battle):
    def __init__(self) -> None:
        super().__init__()

class BossBattle(Battle):
    def __init__(self) -> None:
        super().__init__()