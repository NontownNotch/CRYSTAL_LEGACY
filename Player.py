import pygame

from Settings import *
from Attributes import *

class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        self.imagefront = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.playerfront]
        self.imageback = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.playerback]
        self.imageleft = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.playerleft]
        self.imageright = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.playerright]
        self.images = self.imagefront
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.move = [False, False, False, False]
        self.collide = Collidable()
        self.event = None
        self.tpto = None
        self.HP = PlayerSettings.playerHP
        self.MP = PlayerSettings.playerMP
        self.attack = PlayerSettings.playerAttack
        self.money = PlayerSettings.playerMoney
        self.battlestandimage = pygame.image.load(GamePath.playerbattlestandimage)
        self.battlemagicimages = [pygame.image.load(img) for img in GamePath.playerbattlemagicimage]
        self.battlemagicindex = 0
        self.battlemagicimage = self.battlemagicimages[self.battlemagicindex]
        self.battleattackimage = pygame.image.load(GamePath.playerbattleattackimage)
        self.battleusemagicimage = pygame.image.load(GamePath.playerbattleusemagicimage)
    
    def attr_update(self, addCoins = 0, addHP = 0, addMP = 0):
        if self.money + addCoins < 0:
            return
        elif self.HP < PlayerSettings.playerHP and self.HP + addHP > PlayerSettings.playerHP:
            self.money += addCoins
            self.HP = PlayerSettings.playerHP
            return
        elif self.HP == PlayerSettings.playerHP and self.HP + addHP > PlayerSettings.playerHP:
            return
        elif self.MP < PlayerSettings.playerMP and self.MP + addMP > PlayerSettings.playerMP:
            self.money += addCoins
            self.MP = PlayerSettings.playerMP
            return
        elif self.MP == PlayerSettings.playerMP and self.MP + addMP > PlayerSettings.playerMP:
            return
        elif self.MP + addMP < 0:
            return
        self.money += addCoins
        self.HP += addHP
        self.MP += addMP
    
    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        self.x = x
        self.y = y
    
    def try_move(self, events, maxX = WindowSettings.width, maxY = WindowSettings.height, minX = 0, minY = 0):
        self.dx = self.dy = 0
        #尝试移动
        if events[pygame.K_w]:
            self.move[0] = True
            if self.y - PlayerSettings.playerYSpeed >= minY + PlayerSettings.playerHeight // 2:
                self.dy -= PlayerSettings.playerYSpeed
        if events[pygame.K_s]:
            self.move[1] = True
            if self.y + PlayerSettings.playerYSpeed <= maxY - PlayerSettings.playerHeight //2:
                self.dy += PlayerSettings.playerYSpeed
        if events[pygame.K_a]:
            self.move[2] = True
            if self.x - PlayerSettings.playerXSpeed >= minX + PlayerSettings.playerWidth // 2:
                self.dx -= PlayerSettings.playerXSpeed
        if events[pygame.K_d]:
            self.move[3] = True
            if self.x + PlayerSettings.playerXSpeed <= maxX - PlayerSettings.playerWidth // 2:
                self.dx += PlayerSettings.playerXSpeed
        if events[pygame.K_SPACE]: #加速
            self.dx = self.dx * 2
            self.dy = self.dy * 2
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (self.x, self.y)
    
    def update(self, scene):
        #设置人物图像
        if self.move == [True, False, False, False] or self.move == [True, False, True, True]:
            self.index = (self.index + 1) % 12
            self.images = self.imageback
        elif self.move == [False, True, False, False] or self.move == [False, True, True, True]:
            self.index = (self.index + 1) % 12
            self.images = self.imagefront
        elif self.move == [False, False, True, False] or self.move == [True, False, True, False] or self.move == [False, True, True, False] or self.move == [True, True, True, False]:
            self.index = (self.index + 1) % 12
            self.images = self.imageleft
        elif self.move == [False, False, False, True] or self.move == [True, False, False, True] or self.move == [False, True, False, True] or self.move == [True, True, False, True]:
            self.index = (self.index + 1) % 12
            self.images = self.imageright
        else:
            self.index = 0
        self.image = self.images[self.index]
        self.move = [False, False, False, False]
        #设置人物位置
        testx = Player(self.x - self.dx, self.y)
        testy = Player(self.x, self.y - self.dy)
        if self.collide.is_colliding():
            if self.collide.collidingWith["obstacle"]:
                if pygame.sprite.spritecollide(testy, scene.obstacles, False): #人物移动后碰撞但取消X方向移动后不碰撞
                    self.x -= self.dx
                if pygame.sprite.spritecollide(testx, scene.obstacles, False): #人物移动后碰撞但取消Y方向移动后不碰撞
                    self.y -= self.dy
                self.rect.center = (self.x, self.y)
            if self.collide.collidingWith["portal"]:
                if self.collide.collidingObject["portal"] == 0:
                    self.event = GameEvent.EVENT_SWITCH
                    self.tpto = SceneType.CASTLE
                elif self.collide.collidingObject["portal"] == 1:
                    self.event = GameEvent.EVENT_SWITCH
                    self.tpto = SceneType.TEMPLE
                elif self.collide.collidingObject["portal"] == 2:
                    self.event = GameEvent.EVENT_SWITCH
                    self.tpto = SceneType.HUT
                elif self.collide.collidingObject["portal"] == 3 or self.collide.collidingObject["portal"] == 4:
                    self.event = GameEvent.EVENT_SWITCH
                    self.tpto = SceneType.WILD
            if self.collide.collidingWith["npc"]:
                if self.collide.collidingObject["npc"].name == "Cid":
                    self.event = GameEvent.EVENT_DIALOG
                elif self.collide.collidingObject["npc"].name == "Knight":
                    self.event = GameEvent.EVENT_SHOP
            if self.collide.collidingWith["monster"]:
                self.event = GameEvent.EVENT_BATTLE
        if self.HP <=0:
            self.event = GameEvent.EVENT_RESTART
    
    def draw(self, window, dx=0, dy=0):
        window.blit(self.image, self.rect.move(dx, dy))
    
    def battlemagic(self):
        self.battlemagicindex = (self.battlemagicindex + 1) % 12
        self.battlemagicimage = self.battlemagicimages[self.battlemagicindex]
        return self.battlemagicimage