# -*- coding:utf-8 -*-

import pygame

from typing import *
from Settings import *

class DialogBox:
    def __init__(self, window, npc,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255)):
        self.window = window
        self.background = pygame.transform.scale(pygame.image.load(GamePath.talkboxbackgound), (DialogSettings.boxWidth, DialogSettings.boxHeight))
        self.npc = npc
        self.font = pygame.font.Font(None, fontSize)
        self.dialog = self.font.render(self.npc.dialog, True, fontColor)
        self.exit = self.font.render("[E] Exit", True, fontColor)
    
    def draw(self):
        self.window.blit(self.background, (DialogSettings.boxStartX, DialogSettings.boxStartY))
        self.window.blit(self.dialog, (DialogSettings.textStartX, DialogSettings.textStartY))
        self.window.blit(self.exit, (DialogSettings.textStartX, DialogSettings.textStartY + DialogSettings.textVerticalDist))

class ShoppingBox:
    def __init__(self, window, npc, player,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def buy(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####