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
                 fontColor: Tuple[int, int, int] = (255, 255, 255)):
        self.window = window
        self.background = pygame.transform.scale(pygame.image.load(GamePath.talkboxbackgound), (ShopSettings.boxWidth, ShopSettings.boxHeight))
        self.npc = npc
        self.player = player
        self.font = pygame.font.Font(None, fontSize)
        self.fontcolor = fontColor
        self.text = ["HP + 100 : 10 Coins", "MP + 10 : 5 Coins"]
        self.index = 0
    
    def buy(self):
        if self.index == 0:
            self.player.attr_update(- 10, 100)
        elif self.index == 1:
            self.player.attr_update(- 5, 0, 10)

    def draw(self):
        self.window.blit(self.background, (ShopSettings.boxStartX, ShopSettings.boxStartY))
        if self.index == 0:
            text0 = self.font.render("[E] " + self.text[0], True, self.fontcolor)
            text1 = self.font.render(self.text[1], True, self.fontcolor)
        elif self.index == 1:
            text0 = self.font.render(self.text[0], True, self.fontcolor)
            text1 = self.font.render("[E] " + self.text[1], True, self.fontcolor)
        quit = self.font.render("[Q] Quit", True, self.fontcolor)
        player = self.font.render("HP: " + str(self.player.HP) + " MP: " + str(self.player.MP) + " Money: " + str(self.player.money), True, self.fontcolor)
        self.window.blit(text0, (ShopSettings.textStartX, ShopSettings.textStartY))
        self.window.blit(text1, (ShopSettings.textStartX, ShopSettings.textStartY + ShopSettings.textVerticalDist))
        self.window.blit(quit, (ShopSettings.textStartX, ShopSettings.textStartY + 2 * ShopSettings.textVerticalDist))
        self.window.blit(player, (ShopSettings.textStartX, ShopSettings.textStartY + 3 * ShopSettings.textVerticalDist))