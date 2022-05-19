# Marquat Samuel
# samuel.marquat@etu.univ-lyon1.fr
# Main du jeu PACMAN
# V 0.1

import core
import pygame
from pacman import Pacman
from ghost import Ghost
from fruit import Fruit
from labyrinthe import Labyrinthe


def setup(): #fonction setup
    print("setup")
    core.WINDOW_SIZE = [800,800]
    core.fps = 60
    core.memory("gameOver", False)

    nbGhost = 2
    nbPacman = 1
    nbFruit = 4
    nbFood = 100

    core.memory("score", 0)

    core.memory("tabGhosts", [])
    core.memory("tabPacman", [])
    core.memory("tabFruits", [])
    core.memory("tabFoods", [])

    for i in range (0,nbGhost):
        g = Ghost()
        core.memory("tabGhosts").append(g)

    for t in range (0,nbPacman):
        p = Pacman()
        core.memory("tabPacman").append(p)

    for r in range (0,nbFruit):
        f = Fruit()
        core.memory("tabFruits").append(f)

    for n in range (0,nbFood):
        k = Food()
        core.memory("tabFruits").append(f)



def run(): #fonction run = correspond fps
    print("run")
    Labyrinthe.show()
    core.cleanScreen()

    for i in core.memory("tabGhosts"):
        i.show()
        i.randomMove()
        i.edge()
        i.manger()
        i.mourir()
        gameOver = i.manger(core.memory("pacman"))
        if gameOver:
            core.memory("gameOver", True)

    If not gameOver:
        for t in core.memory("tabPacman"):
            t.show()
            t.moverigth()
            t.moveleft()
            t.moveup()
            t.movedown()
            t.edge()
            t.manger()


    for r in core.memory("tabFruits"):
        r.show()
        r.mourir()
        if r.mourir = True :
            core.memory("score", core.memory("score") + 1)

    for n in core.memory("tabFood"):
        n.show()
        n.mourir()

    police = pygame.font.SysFont('Comic Sans MS', 30)
    texte = police.render('SCORE : ' + str(core.memory("score")), False, (255, 0, 0,))
    core.screen.blit(texte, (core.WINDOW_SIZE[0] / 2 + 650, core.WINDOW_SIZE[1] / 2 - 400))

if __name__ == '__main__':
    core.main(setup,run)

