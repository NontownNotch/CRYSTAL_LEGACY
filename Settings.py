# -*- coding:utf-8 -*-

from enum import Enum
import pygame

class WindowSettings: #窗口设置
    name = "CRYSTAL LEGACY" #标题
    width = 1920 #窗口宽度
    height = 1080 #窗口高度

class SceneSettings:
    tileXnum = 64
    tileYnum = 64
    tileWidth = tileHeight = 64

class PlayerSettings:
    # Initial Player Settings
    playerSpeed = 8
    playerWidth = 64
    playerHeight = 96
    playerHP = 20
    playerMP = 10
    playerAttack = 5
    playerDefence = 1
    playerMoney = 100

class NPCSettings:
    npcSpeed = 1
    npcWidth = 60
    npcHeight = 60

class NPCType(Enum):
    DIALOG = 1
    MONSTER = 2
    SHOP = 3

class SceneType(Enum):
    CITY = 1
    WILD = 2
    BOSS = 3

class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxStartX = WindowSettings.width // 4           # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 + 20 # Coordinate Y of the box

    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 + 10         # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 + 30    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3                # Vertical distance of two lines

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20

class BattleSettings:
    boxWidth = WindowSettings.width #战斗场景宽度
    boxHeight = WindowSettings.height #战斗场景高度
    boxStartX = 0
    boxStartY = 0
    statusStartX = 0 #UI X位置
    statusStartY = WindowSettings.height // 5 * 4 #UI Y位置
    textSize = 48
    textStartX = WindowSettings.width // 4 
    textPlayerStartX = WindowSettings.width // 2          # Coordinate X of the first line of dialog
    textPlayerStatusStartX = WindowSettings.width // 3 * 2
    textMonsterStartX = WindowSettings.width // 6
    textStartY = WindowSettings.height // 15 * 13         # Coordinate Y of the first line of dialog
    ATBStartX = WindowSettings.width // 6 * 5
    textVerticalDist = textSize // 4 * 3            # Vertical distance of two lines

    playerWidth = WindowSettings.width // 15
    playerHeight = WindowSettings.height // 5.625
    playerCoordX = WindowSettings.width // 4 * 3
    playerCoordY = WindowSettings.height // 2 
    playerattackCoordX = WindowSettings.width // 3 * 2

    monsterWidth = WindowSettings.width // 6
    monsterHeight = WindowSettings.height // 3
    monsterCoordX = WindowSettings.width * 5 // 8
    monsterCoordY = WindowSettings.height // 2 

    stepSize = 20

class ShopSettings:
    boxWidth = 800
    boxHeight = 200
    boxStartX = WindowSettings.width // 4   # Coordinate X of the box
    boxStartY = WindowSettings.height // 3  # Coordinate Y of the box

    textSize = 56 # Default font size
    textStartX = boxStartX + 10         # Coordinate X of the first line of dialog
    textStartY = boxStartY + 25    # Coordinate Y of the first line of dialog

class GamePath:
    # Window related path
    menu = r".\assets\MainMenu\MainMenu.png"
    battlebackground = r".\assets\Background\WildBattleBackground.png"

    # player/npc related path
    npc = r".\assets\npc\npc.png"
    playerfront = [
        r".\assets\Player\Front_2.png",
        r".\assets\Player\Front_2.png",
        r".\assets\Player\Front_2.png",
        r".\assets\Player\Front_1.png",
        r".\assets\Player\Front_1.png",
        r".\assets\Player\Front_1.png",
        r".\assets\Player\Front_2.png",
        r".\assets\Player\Front_2.png",
        r".\assets\Player\Front_2.png",
        r".\assets\Player\Front_3.png",
        r".\assets\Player\Front_3.png",
        r".\assets\Player\Front_3.png",
    ]
    playerback = [
        r".\assets\Player\Back_2.png",
        r".\assets\Player\Back_2.png",
        r".\assets\Player\Back_2.png",
        r".\assets\Player\Back_1.png",
        r".\assets\Player\Back_1.png",
        r".\assets\Player\Back_1.png",
        r".\assets\Player\Back_2.png",
        r".\assets\Player\Back_2.png",
        r".\assets\Player\Back_2.png",
        r".\assets\Player\Back_3.png",
        r".\assets\Player\Back_3.png",
        r".\assets\Player\Back_3.png",
    ]
    playerleft = [
        r".\assets\Player\Left_2.png",
        r".\assets\Player\Left_2.png",
        r".\assets\Player\Left_2.png",
        r".\assets\Player\Left_1.png",
        r".\assets\Player\Left_1.png",
        r".\assets\Player\Left_1.png",
        r".\assets\Player\Left_2.png",
        r".\assets\Player\Left_2.png",
        r".\assets\Player\Left_2.png",
        r".\assets\Player\Left_3.png",
        r".\assets\Player\Left_3.png",
        r".\assets\Player\Left_3.png",
    ]
    playerright = [
        r".\assets\Player\Right_2.png",
        r".\assets\Player\Right_2.png",
        r".\assets\Player\Right_2.png",
        r".\assets\Player\Right_1.png",
        r".\assets\Player\Right_1.png",
        r".\assets\Player\Right_1.png",
        r".\assets\Player\Right_2.png",
        r".\assets\Player\Right_2.png",
        r".\assets\Player\Right_2.png",
        r".\assets\Player\Right_3.png",
        r".\assets\Player\Right_3.png",
        r".\assets\Player\Right_3.png",
    ]
    playerbattlestandimage = r".\assets\Player\Battle\Stand.png"
    playerbattlemagicimage = [
        r".\assets\Player\Battle\Magic_1.png",
        r".\assets\Player\Battle\Magic_1.png",
        r".\assets\Player\Battle\Magic_1.png",
        r".\assets\Player\Battle\Magic_1.png",
        r".\assets\Player\Battle\Magic_1.png",
        r".\assets\Player\Battle\Magic_1.png",
        r".\assets\Player\Battle\Magic_2.png",
        r".\assets\Player\Battle\Magic_2.png",
        r".\assets\Player\Battle\Magic_2.png",
        r".\assets\Player\Battle\Magic_2.png",
        r".\assets\Player\Battle\Magic_2.png",
        r".\assets\Player\Battle\Magic_2.png"
    ]
    playerbattleattackimage = r".\assets\Player\Battle\Attack.png"
    playerbattleusemagicimage = r".\assets\Player\Battle\UseMagic.png"
    monster = r".\assets\npc\monster\1.png"
    boss = r".\assets\npc\boss.png"

    #Tiles
    groundTiles = r".\assets\Tiles\Grass.png"
    castlebackground = r".\assets\Background\Castle.png"

    #Obstacles
    tree = [r".\assets\Tiles\Tree.png",
            r".\assets\Tiles\Flower.png"]
    emptyobstacles = r".\assets\Tiles\Empty.png"

    #Portals
    portal = [r".\assets\Portals\Castle.png",
              r".\assets\Portals\Temple.png",
              r".\assets\Portals\Hut.png"]

    #UI
    battlestatus = r".\assets\UI\BattleStatus.png"
    commandbackground = r".\assets\UI\CommandBackground.png"
    ATBbackground = r".\assets\UI\ATBBackground.png"
    ATB = r".\assets\UI\ATB.png"

    #BGM
    bgm = [r".\assets\bgm\city.mp3",
           r".\assets\bgm\wild.mp3",
           r".\assets\bgm\boss.mp3"]

class PortalSettings:
    size = [(128, 128), (128, 128), (128, 128)]
    coordX = (SceneSettings.tileXnum - 10) * SceneSettings.tileWidth / 2
    coordY = (SceneSettings.tileYnum / 2) * SceneSettings.tileHeight / 2

class GameState(Enum):
    MAIN_MENU = 1
    GAME_TRANSITION = 2
    GAME_OVER = 3
    GAME_WIN = 4
    GAME_PAUSE = 5
    GAME_PLAY_WILD = 6
    GAME_PLAY_CASTLE = 7
    GAME_PLAY_TEMPLE = 8
    GAME_PLAY_HUT = 9
    GAME_PLAY_BATTLE = 10
    GAME_PLAY_BOSS = 11

class GameEvent:
    EVENT_BATTLE = pygame.USEREVENT + 1
    EVENT_DIALOG = pygame.USEREVENT + 2
    EVENT_SWITCH = pygame.USEREVENT + 3
    EVENT_RESTART = pygame.USEREVENT + 4
    EVENT_SHOP = pygame.USEREVENT + 5