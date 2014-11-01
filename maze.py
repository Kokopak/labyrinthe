#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)

class Cell:

    def __init__(self, row, col):
        self.init_walls()
        self.row = row
        self.col = col

    def init_walls(self):
        self.n_wall = True
        self.s_wall = True
        self.w_wall = True
        self.e_wall = True

    def all_walls(self):
        return self.n_wall and self.s_wall and self.e_wall and self.w_wall

    def __repr__(self):
        return "<%d, %d>" % (self.row, self.col)

class Maze:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = {}

        self.reset_grid()

    def generate(self):
        self.reset_grid()
        cell_stack = []
        total_cells = self.rows * self.cols
        current_cell = self.grid[(0, 0)]
        visited_cells = 1
        while visited_cells < total_cells :
            neighbors = self.find_neigh(current_cell)
            if len(neighbors) >= 1:
                neigh, direction = random.choice(neighbors)
                if direction == N:
                    current_cell.n_wall = False
                    neigh.s_wall = False
                elif direction == S:
                    current_cell.s_wall = False
                    neigh.n_wall = False
                elif direction == E:
                    current_cell.e_wall = False
                    neigh.w_wall = False
                elif direction == W:
                    current_cell.w_wall = False
                    neigh.e_wall = False
                cell_stack.append(current_cell)
                current_cell = neigh
                visited_cells += 1
            else:
                current_cell = cell_stack.pop()

    def reset_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[(r, c)] = Cell(r, c)

    def find_neigh(self, cell):
        directions = [N, S, E, W]
        neighbors = []
        for d in directions:
            tmp_row, tmp_col = cell.row + d[0], cell.col + d[1]
            if tmp_row >= 0 and tmp_col >= 0 and tmp_row < self.rows and tmp_col < self.cols:
                tmp_neigh = self.grid[(tmp_row, tmp_col)]
                if tmp_neigh.all_walls() :
                    neighbors.append((tmp_neigh, d))

        return neighbors


if __name__ == '__main__':
    maze = Maze(10, 30)
    maze.generate()
