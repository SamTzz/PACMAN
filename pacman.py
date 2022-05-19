# Marquat Samuel
# samuel.marquat@etu.univ-lyon1.fr
# Classe Ghost
# V 0.1

import core
import random
from pygame import Vector2


class Pacman:  # nom de la classe doit commencer par une majuscule
    def __init__(self):  # fonction "__init__" sert a construire notre objet. Fonction "self" dit qu'il se construit tout seul)
        self.couleur = (255, 255, 0)
        self.r = 100
        self.x = random.randint(self.r, core.WINDOW_SIZE[0])
        self.y = random.randint(self.r, core.WINDOW_SIZE[1])

    def show(self):
        core.Draw.circle(self.couleur, [self.x, self.y], self.r)

    def moveup(self):
        if core.getKeyPressList("z"):
            self.y = self.y - 1

    def movedown(self):
        if core.getKeyPressList("s"):
            self.y = self.y + 1

    def moveleft(self):
        if core.getKeyPressList("q"):
            self.x = self.x - 1

    def moveright(self):
        if core.getKeyPressList("d"):
            self.x = self.x + 1

        self.edge()

    def edge(self):
        if self.x - self.r <= 0:
            self.x = self.r

        if self.x + self.r > core.WINDOW_SIZE[0]:
            self.x = core.WINDOW_SIZE[0] - self.r

        if self.y - self.r <= 0:
            self.y = self.r

        if self.y + self.r > core.WINDOW_SIZE[1]:
            self.y = core.WINDOW_SIZE[1] - self.r

