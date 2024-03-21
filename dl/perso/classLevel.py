import pygame
from config import *
from classBackground import Background
from classBee import Bee
from classHero import Hero

class Level():
    def __init__(self, displaySurface):
        self.displaySurface = displaySurface
        self.background = Background()
        self.hero = Hero((400,400), faceRight = True)
        # self.bee1 = Bee((200,200), moveRight=True)
        # self.bee2 = Bee((500,300), moveRight=False)

    def update(self):
        self.hero.update(self)
        # self.bee1.update(self)
        # self.bee2.update(self)

    def draw(self):
        self.background.draw(self.displaySurface)
        self.hero.draw(self.displaySurface)
        # self.bee1.draw(self.displaySurface)
        # self.bee2.draw(self.displaySurface)

    def run(self):
        self.update()
        self.draw()