import numpy as np
import random


class Sudoku:
    def __init__(self) -> None:
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

    def gen(self):
        grid_poss = {}
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    grid_poss[(x, y)] = [
                        i for i in range(1, 10) if self.possible(x, y, i)
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
                self.gen()
                self.grid[y][x] = 0
            return

        self.unique = True
        self.solutions = 0
        self.display()

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

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return
        self.solutions += 1
        if self.solutions > 1:
            self.unique = False
            return
        self.display()


s = Sudoku()
s.solve()
print(s.unique)
