#!/usr/bin/env python

import pygame, sys

pygame.init()

SIZE = (50,50)

class Game:
    def __init__(self, size, squaresize = 10, delay = 500):
        self.squaresize = squaresize
        self.size = size
        self.screen = pygame.display.set_mode((size[0]*squaresize,
            size[1]*squaresize))
        self.cells = []
        for i in xrange(size[0]):
            self.cells.append([])
            for j in xrange(size[1]):
                self.cells[i].append(False)
        self.running = False
        self.alive = pygame.Surface((squaresize,squaresize))
        self.alive.fill((255,255,255))
        self.dead = pygame.Surface((squaresize,squaresize))
        self.dead.fill((0,0,0))
        self.delay = delay
        self.nextstep = 0

        self.clock = pygame.time.Clock()
        self.paused = True

    def SetCell(self, posx, posy, value):
        self.cells[posx][posy] = value

    def GetAt(self, posx, posy):
        while posx < 0: 
            posx += self.size[0]
        while posx >= self.size[0]: 
            posx -= self.size[0]
        while posy < 0: 
            posy += self.size[1]
        while posy >= self.size[1]: 
            posy -= self.size[1]
        if self.cells[posx][posy]:
            return 1
        else:
            return 0

    def Pause(self):
        self.paused = not self.paused

    def Run(self):
        self.running = True
        self.MainLoop()

    def UpdateCells(self):
        # create new list
        cells2 = []
        for i in xrange(self.size[0]):
            cells2.append([])
            for j in xrange(self.size[1]):
                cells2[i].append(False)

        for x in xrange(self.size[0]):
            for y in xrange(self.size[1]):
                num = 0
                num += self.GetAt(x-1, y-1)
                num += self.GetAt(x,   y-1)
                num += self.GetAt(x+1, y-1)
                num += self.GetAt(x-1, y)
                num += self.GetAt(x+1, y)
                num += self.GetAt(x-1, y+1)
                num += self.GetAt(x,   y+1)
                num += self.GetAt(x+1, y+1)
                cells2[x][y] =  (num <= 4 and num >=2)
        self.cells = cells2

    def MainLoop(self):
        self.running = True
        while (self.running):
            self.Update()
            self.HandleEvents()
            self.Draw()

    def Update(self):
        if (self.nextstep <= 0):
            self.nextstep = self.delay
            self.UpdateCells()
        if not self.paused:
            self.nextstep -= self.clock.tick(100)
        pass

    def HandleEvents(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_SPACE:
                    self.Pause()
                if event.key == pygame.K_PLUS and self.delay > 100:
                    self.delay -= 100
                if event.key == pygame.K_MINUS and self.delay < 1000:
                    self.delay += 100
        p = pygame.mouse.get_pressed()
        if p[0]:
            self.SetCell(pygame.mouse.get_pos()[0] / self.squaresize, pygame.mouse.get_pos()[1] / self.squaresize, True)
        elif p[2]:
            self.SetCell(pygame.mouse.get_pos()[0] / self.squaresize,
                    pygame.mouse.get_pos()[1] / self.squaresize, False)

    def Draw(self):
        self.screen.fill((128,128,128))
        for i in xrange(self.size[0]):
            for j in xrange(self.size[1]):
                if self.cells[i][j]:
                    s = self.alive
                else:
                    s = self.dead
                self.screen.blit(s, (i*self.squaresize, j*self.squaresize))
        pygame.display.flip()

if __name__ == "__main__":

    print (4 is int)

    SIZE = (int(sys.argv[1]),int(sys.argv[2]))
    game = Game(SIZE, int(sys.argv[3]), 200)

    game.MainLoop()

