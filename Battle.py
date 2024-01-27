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
        #状态参数
        self.ATB = 0
        self.iscommanding = False #检测是否在Command状态
        self.ismagic = False #检测是否在Magic状态
        self.attackCD = 0
        self.magicCD = 0
        self.monsterCD = 300
        self.monsterattackCD = 0
        #render系列参数
        self.battlestatus = pygame.transform.scale(pygame.image.load(GamePath.battlestatus), (WindowSettings.width, WindowSettings.height // 5)) #设置战斗UI
        self.commandbackground = pygame.transform.scale(pygame.image.load(GamePath.commandbackground), (WindowSettings.width // 8 * 3, WindowSettings.height // 5)) #设置Command与Magic面板UI
        self.ATBbackground = pygame.transform.scale(pygame.image.load(GamePath.ATBbackground), (WindowSettings.width // 15, WindowSettings.height // 50)) #设置ATB条背景
        self.ATBbar = pygame.image.load(GamePath.ATB)
        self.font = pygame.font.Font(None, fontSize)
        self.fontcolor = fontColor
        self.monstername = self.font.render(f"{self.monster.name}", True, fontColor)
        self.playername = self.font.render("Sansan", True, fontColor)
        self.CommandText = self.font.render("[E] Command", True, fontColor)
        self.CancelText = self.font.render("[Q] Cancel", True, fontColor)
        self.AttackText = self.font.render("[F] Attack", True, fontColor)
        self.MagicText = self.font.render("[R] Magic", True, fontColor)
        self.FireText = self.font.render("[Z] Fire 5 MP", True, fontColor)
        self.ThunderText = self.font.render("[X] Thunder 5 MP", True, fontColor)
        self.effects = [pygame.transform.scale(pygame.image.load(GamePath.fireeffect), (BattleSettings.effectWidth, BattleSettings.effectHeight)),
                        pygame.transform.scale(pygame.image.load(GamePath.thundereffect), (BattleSettings.effectWidth, BattleSettings.effectHeight))]
        self.effect = None
        self.effectrect = None
        self.playerimage = None
        self.playerimagerect = None
        self.monsterimage = pygame.transform.scale(monster.image, (BattleSettings.monsterWidth, BattleSettings.monsterHeight))
        self.monsterrect = self.monsterimage.get_rect(center = (BattleSettings.monsterCoordX, BattleSettings.monsterCoordY))
        self.monsterskillbackground = pygame.transform.scale(pygame.image.load(GamePath.skillbackground), (WindowSettings.width // 2, WindowSettings.height // 15))
        self.monsterskill = self.font.render(f"{self.monster.skillname}", True, fontColor)
        self.monsterskillrect = self.monsterskill.get_rect(center = (WindowSettings.width // 2, WindowSettings.height // 30))
    
    def render(self):
        #UI
        self.window.blit(self.battlestatus, (BattleSettings.statusStartX, BattleSettings.statusStartY)) #显示战斗UI
        self.window.blit(self.monstername, (BattleSettings.textMonsterStartX, BattleSettings.textStartY)) #显示怪物名称
        self.window.blit(self.playername, (BattleSettings.textPlayerStartX, BattleSettings.textStartY)) #显示玩家名称
        HP = self.font.render(f"HP {self.player.HP} / {PlayerSettings.playerHP}", True, self.fontcolor)
        MP = self.font.render(f"MP {self.player.MP} / {PlayerSettings.playerMP}", True, self.fontcolor)
        self.window.blit(HP, (BattleSettings.textPlayerStatusStartX, BattleSettings.textStartY)) #显示玩家HP
        self.window.blit(MP, (BattleSettings.textPlayerStatusStartX, BattleSettings.textStartY + BattleSettings.textVerticalDist)) #显示玩家MP
        self.window.blit(self.ATBbackground, (BattleSettings.ATBStartX, BattleSettings.textStartY)) #显示玩家ATB条背景
        self.window.blit(pygame.transform.scale(self.ATBbar, (WindowSettings.width * self.ATB // 2250, WindowSettings.height // 50)), (BattleSettings.ATBStartX, BattleSettings.textStartY))
        if self.ATB == 150 and not self.iscommanding:
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
        #怪物动画
        if self.monsterattackCD == 0:
            self.monsterrect.center = (BattleSettings.monsterCoordX, BattleSettings.monsterCoordY)
            self.window.blit(self.monsterimage, self.monsterrect)
        else:
            self.monsterrect.center = (BattleSettings.mosterattackCoordX, BattleSettings.monsterCoordY)
            self.window.blit(self.monsterimage, self.monsterrect)
            self.window.blit(self.monsterskillbackground, (BattleSettings.skillStartX, BattleSettings.skillStartY))
            self.window.blit(self.monsterskill, self.monsterskillrect)
        #玩家动画
        if not self.ismagic and self.attackCD == 0 and self.magicCD == 0: #站立动画
            self.playerimage = pygame.transform.scale(self.player.battlestandimage, (BattleSettings.playerWidth, BattleSettings.playerHeight))
            self.playerimagerect = self.playerimage.get_rect(center = (BattleSettings.playerCoordX, BattleSettings.playerCoordY))
            self.window.blit(self.playerimage, self.playerimagerect)
        elif self.ismagic: #咏唱魔法动画
            self.playerimage = pygame.transform.scale(self.player.battlemagic(), (BattleSettings.playerWidth, BattleSettings.playerHeight))
            self.playerimagerect = self.playerimage.get_rect(center = (BattleSettings.playerCoordX, BattleSettings.playerCoordY))
            self.window.blit(self.playerimage, self.playerimagerect)
        elif not self.ismagic and self.attackCD != 0:
            self.playerimage = pygame.transform.scale(self.player.battleattackimage, (BattleSettings.playerWidth, BattleSettings.playerHeight))
            self.playerimagerect = self.playerimage.get_rect(center = (BattleSettings.playerattackCoordX, BattleSettings.playerCoordY))
            self.window.blit(self.playerimage, self.playerimagerect)
        elif not self.ismagic and self.magicCD != 0: #使用魔法动画
            self.playerimage = pygame.transform.scale(self.player.battleusemagicimage, (BattleSettings.playerWidth, BattleSettings.playerHeight))
            self.playerimagerect = self.playerimage.get_rect(center = (BattleSettings.playerCoordX, BattleSettings.playerCoordY))
            self.window.blit(self.playerimage, self.playerimagerect)
            self.window.blit(self.effect, self.effectrect)
    
    def ATBmanage(self):
        if self.ATB != 150:
            self.ATB +=1
        if self.attackCD != 0:
            self.attackCD -=1
        if self.magicCD != 0:
            self.magicCD -=1
    
    def Attack(self):
        self.ATB = 0
        self.attackCD = 30
        self.monster.attr_update(- self.player.attack)
    
    def MagicFire(self):
        if self.player.MP > 0:
            self.ATB = 0
            self.magicCD = 60
            self.player.attr_update(0, 0, -5)
            self.monster.attr_update(- self.player.attack * 2)
            self.effect = self.effects[0]
            self.effectrect = self.effect.get_rect(center = (BattleSettings.monsterCoordX, BattleSettings.monsterCoordY))
    
    def MagicThunder(self):
        if self.player.MP > 0:
            self.ATB = 0
            self.magicCD = 60
            self.player.attr_update(0, 0, -5)
            self.monster.attr_update(- self.player.attack * 2)
            self.effect = self.effects[1]
            self.effectrect = self.effect.get_rect(center = (BattleSettings.monsterCoordX, BattleSettings.monsterCoordY))
    
    def MonsterAttack(self):
        self.player.attr_update(0, - self.monster.attack)
        self.monsterattackCD = 30

    def Update(self):
        if self.monsterCD > 0:
            self.monsterCD -= 1
        else:
            self.MonsterAttack()
            self.monsterCD = 300
        if self.monsterattackCD != 0:
            self.monsterattackCD -= 1
        if self.monster.HP <= 0:
            self.player.event = GameEvent.EVENT_END_BATTLE
            self.player.attr_update(self.monster.money)
        if self.player.HP <= 0:
            self.player.event = GameEvent.EVENT_RESTART
        

class MonsterBattle(Battle):
    def __init__(self, window, player, monster):
        super().__init__(window, player, monster)
        self.background = pygame.transform.scale(pygame.image.load(GamePath.battlebackground), (WindowSettings.width, WindowSettings.height))
    
    def render(self):
        self.window.blit(self.background,(BattleSettings.boxStartX, BattleSettings.boxStartY)) #显示战斗背景
        return super().render()

class BossBattle(Battle):
    def __init__(self, window, player, monster):
        super().__init__(window, player, monster)
        self.monsterimage = pygame.transform.scale(monster.image, (WindowSettings.width * 4 // 15, WindowSettings.height * 7 // 18))
        self.monsterrect = self.monsterimage.get_rect(center = (BattleSettings.monsterCoordX, BattleSettings.monsterCoordY))
        self.background = pygame.transform.scale(pygame.image.load(GamePath.bossbackground), (WindowSettings.width, WindowSettings.height))
    
    def render(self):
        self.window.blit(self.background,(BattleSettings.boxStartX, BattleSettings.boxStartY))
        return super().render()