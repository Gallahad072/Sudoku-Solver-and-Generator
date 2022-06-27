import numpy as np
import random


class Sudoku:
    def __init__(self) -> None:
        self.gen(False)

    def display(self):
        print(np.matrix(self.grid))

    def possible(self, x, y, n):
        for i in range(9):
            if n in (self.grid[y][i], self.grid[i][x]):
                return False
        x0, y0 = (x // 3) * 3, (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[y0 + i][x0 + j] == n:
                    return False
        return True

    def getValidBoard(self, display=True):
        self.found = False
        grid_poss = {}
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    grid_poss[(x, y)] = [
                        n for n in range(1, 10) if self.possible(x, y, n)
                    ]
        if len(grid_poss) > 0:
            min_len = min(len(v) for v in grid_poss.values())
            if min_len == 0:
                return
            (x, y), v = random.choice(
                [(k, v) for k, v in grid_poss.items() if len(v) == min_len]
            )
            for val in v:
                self.grid[y][x] = val
                self.getValidBoard(display)
                if self.found:
                    return
                self.grid[y][x] = 0
            return

        self.found = True
        if display:
            self.display()

    def solve(self, display=True, unique=None):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.grid[y][x] = n
                            unique = self.solve(display, unique)
                            if unique is False:
                                return unique
                            self.grid[y][x] = 0
                    return unique

        if unique is None:
            unique = True
            if display:
                self.display()
        elif unique is True:
            unique = False

        return unique

    def getProblem(self, display=True):
        self.getValidBoard(False)
        pairs = [(i, j) for i, j in zip(range(41), range(80, 41, -1))]
        random.shuffle(pairs)
        for i, j in pairs:
            temp1 = self.grid[i // 9][i % 9]
            temp2 = self.grid[j // 9][j % 9]
            self.grid[i // 9][i % 9] = 0
            self.grid[j // 9][j % 9] = 0
            if not self.solve(False):
                self.grid[i // 9][i % 9] = temp1
                self.grid[j // 9][j % 9] = temp2
        if display:
            self.display()

    def gen(self, display=True):
        self.grid = []
        while [x for xx in self.grid for x in xx].count(0) < 36:
            self.grid = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
            self.getProblem(False)
        if display:
            self.display()


s = Sudoku()
s.gen()
s.solve()
