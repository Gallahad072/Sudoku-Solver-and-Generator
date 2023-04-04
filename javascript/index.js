class Sudoku {
  constructor() {
    this.gen(false);
  }

  display() {
    let temp, element;
    console.log();
    for (let i = 0; i < 9; i++) {
      if (i % 3 == 0) {
        console.log("  -----------------------------");
      }
      temp = [];
      temp.push(" | ");
      for (let j = 0; j < 9; j++) {
        element = this.grid[i][j];
        if (element == 0) {
          temp.push(" ");
        } else {
          temp.push(String(element));
        }
        if (j % 3 == 2) {
          temp.push(" | ");
        }
      }
      console.log(temp.join(" "));
      // TODO add [:-2]
    }
    console.log("  -----------------------------");
  }

  possible(x, y, n) {
    for (let i = 0; i < 9; i++) {
      if (n in [this.grid[y][i], this.grid[i][x]]) {
        return false;
      }
    }
    let x0, y0;
    x0, (y0 = Math.floor(x / 3) * 3), Math.floor(y / 3) * 3;
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (this.grid[y0 + i][x0 + j] == n) {
          return false;
        }
      }
    }
    return true;
  }

  getValidBoard() {
    let grid_poss = {};
    for (let y = 0; y < 9; y++) {
      for (let x = 0; x < 9; x++) {
        if (this.grid[y][x] == 0) {
          grid_poss[(x, y)] = [];
          for (let n = 1; n < 10; n++) {
            if (this.possible(x, y, n)) {
              grid_poss[(x, y)].push(n);
            }
          }
        }
      }
    }
    if (grid_poss.length > 0) {
      min_len = Math.min(...Object.values(grid_poss).map((x) => x.length));
      if (min_len == 0) {
        return false;
      }
      temp = Object.entries(grid_poss).filter((x) => x[1].length == min_len);
      (x, y), (v = temp[Math.floor(Math.random() * temp.length)]);
      for (let n of v) {
        this.grid[y][x] = n;
        if (this.getValidBoard()) {
          return false;
        }
        this.grid[y][x] = 0;
      }
      return false;
    }
    return true;
  }

  solveAlgo() {
    for (let y = 0; y < 9; y++) {
      for (let x = 0; x < 9; x++) {
        if (this.grid[y][x] == 0) {
          for (let n = 1; n < 10; n++) {
            if (this.possible(x, y, n)) {
              this.grid[y][x] = n;
              this.solveAlgo();
              if (this.unique == false) {
                return false;
              }
              this.grid[y][x] = 0;
            }
          }
          return false;
        }
      }
    }
    if (this.unique == null) {
      this.unique = true;
    } else if (this.unique == true) {
      this.unique = false;
    }
  }

  solve() {
    this.unique = null;
    this.solveAlgo();
    return this.unique;
  }
  shuffle(array) {
    let currentIndex = array.length,
      randomIndex;
    while (currentIndex != 0) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex],
        array[currentIndex],
      ];
    }
    return array;
  }
  // FIXME
  getProblem() {
    this.getValidBoard(false);
    let pairs = [];
    for (let i = 0; i < 41; i++) {
      pairs.push([i, 80 - i]);
    }
    this.shuffle(pairs);
    for (let [i, j] of pairs) {
      let temp1, temp2;
      temp1 = this.grid[Math.floor(i / 9)][i % 9];
      temp2 = this.grid[Math.floor(j / 9)][j % 9];
      this.grid[Math.floor(i / 9)][i % 9] = 0;
      this.grid[Math.floor(j / 9)][j % 9] = 0;
      if (!this.solve(false)) {
        this.grid[Math.floor(i / 9)][i % 9] = temp1;
        this.grid[Math.floor(j / 9)][j % 9] = temp2;
      }
    }
  }
  // FIXME
  gen() {
    this.grid = [];
    // while (this.grid.flat().filter((x) => x == 0).length < 30) {
    //   this.grid = [];
    //   for (let i = 0; i < 9; i++) {
    //     this.grid.push([]);
    //     for (let j = 0; j < 9; j++) {
    //       this.grid[i].push([0]);
    //     }
    //   }
    //   this.getProblem(false);
    // }
    this.grid = [];
    for (let i = 0; i < 9; i++) {
      this.grid.push([]);
      for (let j = 0; j < 9; j++) {
        this.grid[i].push([0]);
      }
    }
    this.getProblem(false);
  }
}

s = new Sudoku();
s.display();
s.solve();
s.display();
