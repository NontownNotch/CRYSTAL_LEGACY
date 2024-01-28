# -*- coding:utf-8 -*-

from enum import Enum
import pygame

#窗口相關設置
class WindowSettings: #窗口設置
    name = "CRYSTAL LEGACY" #標題
    width = 1280 #窗口寬度
    height = 720 #窗口高度

#場景相關設置
class SceneSettings:
    tileXnum = 64
    tileYnum = 64
    tileWidth = WindowSettings.width // 30 #Tile寬度
    tileHeight = WindowSettings.height * 8 // 135 #Tile高度

class PortalSettings:
    size = [(SceneSettings.tileWidth * 4, SceneSettings.tileHeight * 4), (SceneSettings.tileWidth * 4, SceneSettings.tileHeight * 4), (SceneSettings.tileWidth * 2, SceneSettings.tileHeight * 2), (SceneSettings.tileWidth, SceneSettings.tileHeight), (SceneSettings.tileWidth * 3, SceneSettings.tileHeight)] #Portal大小

#玩家相關設置
class PlayerSettings:
    #玩家設置
    playerXSpeed = WindowSettings.width // 240 #人物X方向速度
    playerYSpeed = WindowSettings.height // 135 #人物Y方向速度
    playerWidth = WindowSettings.width // 30 #人物宽度
    playerHeight = WindowSettings.height * 4 // 45 #人物高度
    playerHP = 1000
    playerMP = 100
    playerAttack = 200
    playerMoney = 100

#NPC, 怪物相關設置
class NPCSettings:
    npcWidth = WindowSettings.width // 30
    npcHeight = WindowSettings.height * 4 // 45

class MonsterSettings:
    monsterSpeed = WindowSettings.width // 240
    monsterWidth = WindowSettings.width // 15
    monsterHeight = WindowSettings.height * 16 // 135

class NPCType(Enum):
    DIALOG = 1
    MONSTER = 2
    SHOP = 3

class SceneType(Enum):
    WILD = 1
    CASTLE = 2
    TEMPLE = 3
    HUT = 4
    TITLE = 5
    BATTLE = 6
    BOSS = 7

class DialogSettings:
    boxWidth = WindowSettings.width // 2
    boxHeight = WindowSettings.height // 5
    boxStartX = WindowSettings.width // 4           # Coordinate X of the box
    boxStartY = 0 # Coordinate Y of the box

    textSize = int(pow(WindowSettings.width * WindowSettings.height, 0.5) // 30) # Default font size
    textStartX = WindowSettings.width // 4 + 36         # Coordinate X of the first line of dialog
    textStartY = boxHeight // 3    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3                # Vertical distance of two lines

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20

#戰鬥相關設置
class BattleSettings:
    #UI設置
    boxWidth = WindowSettings.width #戰鬥場景寬度
    boxHeight = WindowSettings.height #戰鬥場景高度
    boxStartX = 0 #戰鬥場景X位置
    boxStartY = 0 #戰鬥場景Y位置
    statusStartX = 0 #UI X位置
    statusStartY = WindowSettings.height // 5 * 4 #UI Y位置
    skillStartX = WindowSettings.width // 4
    skillStartY = 0
    effectWidth = WindowSettings.width // 15
    effectHeight = WindowSettings.height * 8 // 45
    textSize = int(pow(WindowSettings.width * WindowSettings.height, 0.5) // 30) #字體大小
    textPlayerStartX = WindowSettings.width // 2 #玩家文字X位置
    textPlayerStatusStartX = WindowSettings.width // 3 * 2 #玩家狀態文字X位置
    textMonsterStartX = WindowSettings.width // 6 #怪物文字X位置
    textStartY = WindowSettings.height // 15 * 13 #文字Y位置
    ATBStartX = WindowSettings.width // 6 * 5 #ATB條X位置
    textVerticalDist = textSize // 4 * 3 #文字行間距

    #玩家設置
    playerWidth = WindowSettings.width // 15 #玩家寬度
    playerHeight = WindowSettings.height * 8 // 45 #玩家高度
    playerCoordX = WindowSettings.width * 3 // 4 #玩家X位置
    playerCoordY = WindowSettings.height // 2 #玩家Y位置
    playerattackCoordX = WindowSettings.width // 3 * 2 #玩家Attack X位置

    #怪物設置
    monsterWidth = WindowSettings.width * 2 // 15
    monsterHeight = WindowSettings.height * 32 // 135
    monsterCoordX = WindowSettings.width // 4
    monsterCoordY = WindowSettings.height // 2
    mosterattackCoordX = WindowSettings.width // 3

class ShopSettings:
    boxWidth = WindowSettings.width // 2
    boxHeight = WindowSettings.height // 5
    boxStartX = WindowSettings.width // 4   # Coordinate X of the box
    boxStartY = 0  # Coordinate Y of the box
    textSize = int(pow(WindowSettings.width * WindowSettings.height, 0.5) // 30) # Default font size
    textStartX = boxStartX + WindowSettings.width // 192         # Coordinate X of the first line of dialog
    textStartY = boxStartY + WindowSettings.height * 5 // 216    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize * 3 // 4

#文件位置
class GamePath:
    #窗口相關文件位置
    menu = r".\assets\MainMenu\MainMenu.png" #主菜單
    battlebackground = r".\assets\Background\WildBattleBackground.png" #戰鬥背景
    bossbackground = r".\assets\Background\BossBattleBackground.png"

    #Tile相關位置
    groundTiles = r".\assets\Tiles\Grass.png" #草地圖像
    castlebackground = r".\assets\Background\Castle.png" #Castle背景
    templebackground = r".\assets\Background\Temple.png" #Temple背景
    hutbackground = r".\assets\Background\Hut.png" #Hut背景

    #Obstacle相關位置
    tree = [
        r".\assets\Tiles\Tree.png",
        r".\assets\Tiles\Flower.png"
    ] #樹圖像
    emptyobstacles = r".\assets\Tiles\Empty.png" #空圖像

    #Portal相關位置
    portal = [r".\assets\Portals\Castle.png",
              r".\assets\Portals\Temple.png",
              r".\assets\Portals\Hut.png",
              r".\assets\Tiles\Empty.png",
              r".\assets\Tiles\Empty.png"]
    
    #玩家相關位置
    cid = r".\assets\NPC\Cid.png"
    knight = r".\assets\NPC\Knight.png"
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
    ] #玩家前朝向圖像
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
    ] #玩家後朝向圖像
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
    ] #玩家左朝向圖像
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
    ] #玩家右朝向圖像
    playerbattlestandimage = r".\assets\Player\Battle\Stand.png" #玩家戰鬥Stand圖像
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
    ] #玩家戰鬥Magic圖像
    playerbattleattackimage = r".\assets\Player\Battle\Attack.png" #玩家戰鬥Attack圖像
    playerbattleusemagicimage = r".\assets\Player\Battle\UseMagic.png" #玩家戰鬥Use Magic圖像
    fireeffect = r".\assets\Effects\Fire.png"
    thundereffect = r".\assets\Effects\Thunder.png"
    monster = r".\assets\Monster\Sweeper.png"
    boss = r".\assets\Boss\Bahamut.png"

    #UI相關位置
    talkboxbackgound = r".\assets\UI\Talkbox.png"
    battlestatus = r".\assets\UI\BattleStatus.png" #戰鬥Status UI背景
    commandbackground = r".\assets\UI\CommandBackground.png" #戰鬥Command UI背景
    skillbackground = r".\assets\UI\Skill.png"
    ATBbackground = r".\assets\UI\ATBBackground.png" #戰鬥ATB條背景
    ATB = r".\assets\UI\ATB.png" #戰鬥ATB條

    #BGM相關位置
    bgm = {"prelude": r".\assets\BGM\Prelude.mp3",
           "castle": r".\assets\BGM\Castle.mp3",
           "wild": r".\assets\BGM\Wild.mp3",
           "temple": r".\assets\BGM\Temple.mp3",
           "hut": r".\assets\BGM\Hut.mp3",
           "battle": r".\assets\BGM\Battle.mp3",
           "boss": r".\assets\BGM\Boss.mp3"}

#游玩狀態
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
    EVENT_END_BATTLE = pygame.USEREVENT + 6