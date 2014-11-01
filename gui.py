#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from maze import Maze

SIZE_CELL = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (120, 255, 0)

class Gui:

    def __init__(self, rows, cols):
        pygame.init()

        self.rows = rows
        self.cols = cols

        self.maze = Maze(self.rows, self.cols)
        self.maze.generate()
        self.screen = pygame.display.set_mode((self.cols * SIZE_CELL, self.rows*SIZE_CELL))

        pygame.display.set_caption("OnlineByrinth")

        self.show_solution = False

        self.quit = False

    def update(self):
        return

    def draw(self):
        self.screen.fill((WHITE))
        for pos, cell in self.maze.grid.items():
            row, col = pos
            row, col = row * SIZE_CELL, col * SIZE_CELL
            if cell.n_wall:
                pygame.draw.line(self.screen, RED, (col, row), (col + SIZE_CELL, row))
            if cell.s_wall:
                pygame.draw.line(self.screen, RED, (col, row + SIZE_CELL), (col + SIZE_CELL, row + SIZE_CELL))
            if cell.w_wall:
                pygame.draw.line(self.screen, RED, (col, row), (col, row + SIZE_CELL))
            if cell.e_wall:
                pygame.draw.line(self.screen, RED, (col + SIZE_CELL, row), (col + SIZE_CELL, row + SIZE_CELL))

        if self.show_solution:
            for cell in self.maze.path:
                row, col = cell.row * SIZE_CELL, cell.col * SIZE_CELL
                pygame.draw.ellipse(self.screen, GREEN, pygame.Rect(col + SIZE_CELL / 4, row + SIZE_CELL / 4, SIZE_CELL / 2, SIZE_CELL / 2))

        pygame.display.flip()

    def main_loop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit = True
                if event.type == KEYDOWN and event.key == pygame.K_SPACE:
                    self.maze.generate()
                if event.type == KEYDOWN and event.key == pygame.K_s:
                    self.show_solution = not self.show_solution
            self.update()
            self.draw()


if __name__ == '__main__':
    gui = Gui(30, 50)
    gui.main_loop()
