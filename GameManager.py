import sys
import pygame

from Player import Player
from Scene import *
from Settings import *
from PopUpBox import *
from Battle import *
from Monster import *
from BgmPlayer import *

class GameManager:
    def __init__(self):
        self.window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height)) #初始化窗口
        self.title = pygame.display.set_caption(WindowSettings.name) #初始化标题
        self.clock = pygame.time.Clock()
        self.player = Player(WindowSettings.width // 2, WindowSettings.height // 2)
        self.state = GameState.MAIN_MENU #设置初始状态为主界面
        self.scene = MainMenu(self.window)
        self.popupscene = None
    
    def game_reset(self):
        self.player = Player(WindowSettings.width // 2, WindowSettings.height // 2)
        self.state = GameState.MAIN_MENU #设置初始状态为主界面
        self.scene = MainMenu(self.window)
        self.popupscene = None
    
    # Necessary game components here ↓
    def tick(self, fps):
        self.clock.tick(fps)
    
    def get_time(self):
        return self.clock.get_time()
    
    # Scene-related update functions here ↓
    def flush_scene(self, GOTO:SceneType):
        if GOTO == SceneType.WILD:
            self.scene = WildScene(self.window)
            self.state = GameState.GAME_PLAY_WILD
            self.scene.gen_WILD()
        elif GOTO == SceneType.CASTLE:
            self.scene = CastleScene(self.window)
            self.state = GameState.GAME_PLAY_CASTLE
            self.scene.gen_castle()
            self.player.reset_pos(WindowSettings.width // 2, WindowSettings.height * 248 // 27)
        elif GOTO == SceneType.TEMPLE:
            self.scene = TempleScene(self.window)
            self.state = GameState.GAME_PLAY_TEMPLE
            self.scene.gen_temple()
            self.player.reset_pos(WindowSettings.width // 2, WindowSettings.height * 1244 // 135)
        elif GOTO == SceneType.HUT:
            self.scene = HutScene(self.window)
            self.state = GameState.GAME_PLAY_HUT
            self.scene.gen_hut()
            self.player.reset_pos(WindowSettings.width * 11 // 20, WindowSettings.height * 1228 // 135)

    
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
                self.flush_scene(SceneType.CASTLE)
    
    def update_wild(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT: #退出游戲
                pygame.quit()
                sys.exit()
        self.player.try_move(pygame.key.get_pressed(), self.scene.maxX, self.scene.maxY) #嘗試移動
        if self.player.event == GameEvent.EVENT_SWITCH:
            self.flush_scene(self.player.tpto)
        elif self.player.event == GameEvent.EVENT_BATTLE:
            self.state = GameState.GAME_PLAY_BATTLE
            self.popupscene = MonsterBattle(self.window, self.player, self.player.collide.collidingObject["monster"])
        self.player.event = None
        
        # Then deal with regular updates
        self.update_collide()
        self.player.update(self.scene)
        for monster in self.scene.monsters:
            monster.update()
    
    def update_castle(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if self.scene.istalking:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.player.collide.collidingObject["npc"].talkCD = 60
                        self.scene.end_dialog()
            return
        self.player.try_move(pygame.key.get_pressed(), self.scene.maxX, self.scene.maxY, self.scene.minX, self.scene.minY) #嘗試移動
        if self.player.event == GameEvent.EVENT_SWITCH:
            self.flush_scene(self.player.tpto)
            self.player.reset_pos(WindowSettings.width * 23 // 12, SceneSettings.tileYnum * SceneSettings.tileHeight // 2)
        elif self.player.event == GameEvent.EVENT_DIALOG:
            self.scene.trigger_dialog(self.player.collide.collidingObject["npc"])
        self.player.event = None

        # Then deal with regular updates
        self.update_collide()
        self.player.update(self.scene)
        for npc in self.scene.npcs:
            npc.update()
    
    def update_temple(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.player.try_move(pygame.key.get_pressed(), self.scene.maxX, self.scene.maxY, self.scene.minX, self.scene.minY) #嘗試移動
        if self.player.event == GameEvent.EVENT_SWITCH:
            self.flush_scene(self.player.tpto)
            self.player.reset_pos(WindowSettings.width * 13 // 60, SceneSettings.tileYnum * SceneSettings.tileHeight // 2)
        elif self.player.event == GameEvent.EVENT_BATTLE:
            self.state = GameState.GAME_PLAY_BOSS
            self.popupscene = BossBattle(self.window, self.player, self.player.collide.collidingObject["monster"])
        self.player.event = None

        # Then deal with regular updates
        self.update_collide()
        self.player.update(self.scene)
    
    def update_hut(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if self.scene.istalking:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.scene.popupbox.index = (self.scene.popupbox.index - 1) % 2
                    elif event.key == pygame.K_s:
                        self.scene.popupbox.index = (self.scene.popupbox.index + 1) % 2
                    elif event.key == pygame.K_e:
                        self.scene.popupbox.buy()
                    elif event.key == pygame.K_q:
                        self.player.collide.collidingObject["npc"].talkCD = 60
                        self.scene.end_shop()
            return
        self.player.try_move(pygame.key.get_pressed(), self.scene.maxX, self.scene.maxY, self.scene.minX, self.scene.minY) #嘗試移動
        if self.player.event == GameEvent.EVENT_SWITCH:
            self.flush_scene(self.player.tpto)
            self.player.reset_pos(SceneSettings.tileYnum * SceneSettings.tileHeight // 2, WindowSettings.height * 404 // 135)
        elif self.player.event == GameEvent.EVENT_SHOP:
            self.scene.trigger_shop(self.player.collide.collidingObject["npc"], self.player)
        self.player.event = None

        # Then deal with regular updates
        self.update_collide()
        self.player.update(self.scene)
        for npc in self.scene.npcs:
            npc.update()
    
    def update_battle(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if self.popupscene.ATB == 150 and not self.popupscene.iscommanding:
                        self.popupscene.iscommanding = True #开启Command面板
                elif event.key == pygame.K_q:
                    if self.popupscene.iscommanding and not self.popupscene.ismagic:
                        self.popupscene.iscommanding = False #关闭Command面板
                    elif self.popupscene.iscommanding and self.popupscene.ismagic:
                        self.popupscene.ismagic = False #关闭Magic面板
                elif event.key == pygame.K_f:
                    if self.popupscene.iscommanding and not self.popupscene.ismagic:
                        self.popupscene.Attack() #Attack
                        self.popupscene.iscommanding = False
                elif event.key == pygame.K_r:
                    if self.popupscene.iscommanding and not self.popupscene.ismagic:
                        self.popupscene.ismagic = True #开启Magic面板
                elif event.key == pygame.K_z:
                    if self.popupscene.iscommanding and self.popupscene.ismagic:
                        self.popupscene.MagicFire() #使用Fire魔法
                        self.popupscene.ismagic = False
                        self.popupscene.iscommanding = False
                elif event.key == pygame.K_x:
                    if self.popupscene.iscommanding and self.popupscene.ismagic:
                        self.popupscene.MagicThunder() #使用Thunder魔法
                        self.popupscene.ismagic = False
                        self.popupscene.iscommanding = False
        if self.player.event == GameEvent.EVENT_END_BATTLE:
            self.state = GameState.GAME_PLAY_WILD
            return
        elif self.player.event == GameEvent.EVENT_RESTART:
            self.game_reset()
            return
        self.player.event = None

        # Then deal with regular updates
        self.popupscene.ATBmanage() #管理ATB
        self.popupscene.Update()
    
    def update_boss(self, events):
        # Deal with EventQueue First
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if self.popupscene.ATB == 150 and not self.popupscene.iscommanding:
                        self.popupscene.iscommanding = True #开启Command面板
                elif event.key == pygame.K_q:
                    if self.popupscene.iscommanding and not self.popupscene.ismagic:
                        self.popupscene.iscommanding = False #关闭Command面板
                    elif self.popupscene.iscommanding and self.popupscene.ismagic:
                        self.popupscene.ismagic = False #关闭Magic面板
                elif event.key == pygame.K_f:
                    if self.popupscene.iscommanding and not self.popupscene.ismagic:
                        self.popupscene.Attack() #Attack
                        self.popupscene.iscommanding = False
                elif event.key == pygame.K_r:
                    if self.popupscene.iscommanding and not self.popupscene.ismagic:
                        self.popupscene.ismagic = True #开启Magic面板
                elif event.key == pygame.K_z:
                    if self.popupscene.iscommanding and self.popupscene.ismagic:
                        self.popupscene.MagicFire() #使用Fire魔法
                        self.popupscene.ismagic = False
                        self.popupscene.iscommanding = False
                elif event.key == pygame.K_x:
                    if self.popupscene.iscommanding and self.popupscene.ismagic:
                        self.popupscene.MagicThunder() #使用Thunder魔法
                        self.popupscene.ismagic = False
                        self.popupscene.iscommanding = False
        if self.player.event == GameEvent.EVENT_END_BATTLE:
            self.game_reset()
            return
        elif self.player.event == GameEvent.EVENT_RESTART:
            self.game_reset()
            return
        self.player.event = None
        
        # Then deal with regular updates
        self.popupscene.ATBmanage() #管理ATB
        self.popupscene.Update()

    # Collision-relate update funtions here ↓
    def update_collide(self):
        #Obstacles
        if pygame.sprite.spritecollide(self.player, self.scene.obstacles, False):
            self.player.collide.collidingWith["obstacle"] = True
        else:
            self.player.collide.collidingWith["obstacle"] = False
        
        #Portal
        if pygame.sprite.spritecollide(self.player, self.scene.portal, False):
            self.player.collide.collidingWith["portal"] = True
            self.player.collide.collidingObject["portal"] = pygame.sprite.spritecollide(self.player, self.scene.portal, False)[0].index
        else:
            self.player.collide.collidingWith["portal"] = False
            self.player.collide.collidingObject["portal"] = None

        # Player -> NPCs; if multiple NPCs collided, only first is accepted and dealt with.
        if pygame.sprite.spritecollide(self.player, self.scene.npcs, False):
            self.player.collide.collidingWith["npc"] = True
            self.player.collide.collidingObject["npc"] = pygame.sprite.spritecollide(self.player, self.scene.npcs, False)[0]
        else:
            self.player.collide.collidingWith["npc"] = False
            self.player.collide.collidingObject["npc"] = None

        # Player -> Monsters
        if pygame.sprite.spritecollide(self.player, self.scene.monsters, False):
            self.player.collide.collidingWith["monster"] = True
            self.player.collide.collidingObject["monster"] = pygame.sprite.spritecollide(self.player, self.scene.monsters, True)[0]
        else:
            self.player.collide.collidingWith["monster"] = False
            self.player.collide.collidingObject["monster"] = None
    
    # Render-relate update functions here ↓
    def render(self):
        if self.state == GameState.MAIN_MENU:
            self.render_main_menu()
        if self.state == GameState.GAME_PLAY_WILD:
            self.render_wild()
        if self.state == GameState.GAME_PLAY_CASTLE:
            self.render_castle()
        if self.state == GameState.GAME_PLAY_TEMPLE:
            self.render_temple()
        if self.state == GameState.GAME_PLAY_HUT:
            self.render_hut()
        if self.state == GameState.GAME_PLAY_BATTLE:
            self.render_battle()
        if self.state == GameState.GAME_PLAY_BOSS:
            self.render_boss()
    
    def render_main_menu(self):
        self.scene.render() #渲染主界面
    
    def render_wild(self):
        self.scene.update_camera(self.player) #更新Camera位置
        self.scene.render(self.player) #渲染野外场景
    
    def render_castle(self):
        self.scene.update_camera(self.player)
        self.scene.render(self.player)
    
    def render_temple(self):
        self.scene.update_camera(self.player)
        self.scene.render(self.player)
    
    def render_hut(self):
        self.scene.update_camera(self.player)
        self.scene.render(self.player)
    
    def render_battle(self):
        self.popupscene.render() #渲染战斗场景
    
    def render_boss(self):
        self.popupscene.render()