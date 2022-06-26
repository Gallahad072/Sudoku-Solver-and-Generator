import numpy as np
import random


class Sudoku:
    def __init__(self) -> None:
        self.grid = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0],
        ]
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
        self.display()

    def gen(self):
        empty = 0
        grid_poss = {}
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    grid_poss[(x, y)] = [
                        i + 1 for i in range(9) if self.possible(x, y, i + 1)
                    ]
                    empty += 1
        if empty:
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
        self.display()
        input("")

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
        self.display()
        input("Another Solution?")


s = Sudoku()
s.gen()
