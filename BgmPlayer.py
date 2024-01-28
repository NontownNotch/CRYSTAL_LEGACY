import pygame
from Settings import *

class BgmPlayer():
    def __init__(self):
        pygame.mixer.init()
        self.music = GamePath.bgm

    def play(self, name, loop=-1):
        pygame.mixer.music.load(self.music[name])
        pygame.mixer.music.play(loop)

    def stop(self):
        pygame.mixer.music.stop()

    def update(self, GOTO):
        self.stop()
        if GOTO == SceneType.CASTLE:
            self.play("castle")
        elif GOTO == SceneType.WILD:
            self.play("wild")
        elif GOTO == SceneType.TEMPLE:
            self.play("temple")
        elif GOTO == SceneType.HUT:
            self.play("hut")
        elif GOTO == SceneType.TITLE:
            self.play("prelude")
        elif GOTO == SceneType.BATTLE:
            self.play("battle")
        elif GOTO == SceneType.BOSS:
            self.play("boss")