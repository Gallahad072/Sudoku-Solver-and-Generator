import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class Sudoku {
    private int[][] grid;
    private boolean unique;
    private boolean searching;

    Sudoku() {
        this.grid = new int[9][9];
        this.unique = false;
        this.searching = true;
        gen(false);
    }

    private boolean possible(int x, int y, int n) {
        for (int i = 0; i < 9; i++) {
            if ((n == grid[y][i]) || (n == grid[i][x])) {
                return false;
            }
        }
        int x0 = Math.floorDiv(x, 3) * 3;
        int y0 = Math.floorDiv(y, 3) * 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[y0 + i][x0 + j] == n) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean getValidBoard(boolean display) {
        List<int[][]> grid_poss = new ArrayList<>();
        for (int y = 0; y < 9; y++) {
            for (int x = 0; x < 9; x++) {
                if (grid[y][x] == 0) {
                    Set<Integer> ns = new HashSet<>();
                    for (int n = 1; n < 10; n++) {
                        if (possible(x, y, n)) {
                            ns.add(n);
                        }
                    }
                    int[] array = new int[ns.size()];
                    Integer[] tempArray = new Integer[ns.size()];
                    ns.toArray(tempArray);
                    int i = 0;
                    for (Integer n : ns) {
                        array[i] = n;
                        i++;
                    }
                    grid_poss.add(new int[][]{new int[]{x, y}, array});
                }
            }
        }
        if (grid_poss.size() > 0) {
            int min_len = 9;
            for (int[][] positions : grid_poss) {
                int len = positions[1].length;
                if (len == 0) {
                    return false;
                } else if (len < min_len) {
                    min_len = len;
                }
            }
            List<int[][]> filteredPoss = new ArrayList<>();
            for (int[][] poss : grid_poss) {
                if (poss[1].length == min_len) {
                    filteredPoss.add(poss);
                }
            }
            int[][][] filteredArray = new int[filteredPoss.size()][][];
            filteredPoss.toArray(filteredArray);

            Random rand = new Random();
            int[][] randomElement = filteredArray[rand.nextInt(filteredPoss.size())];
            int x = randomElement[0][0];
            int y = randomElement[0][1];
            int[] v = randomElement[1];

            for (int val : v) {
                grid[y][x] = val;
                if (getValidBoard(display)) {
                    return false;
                }
                grid[y][x] = 0;
            }
            return false;
        }
        if (display) {
            display();
        }
        return true;
    }

    private void shuffleArray(int[][] ar) {
        Random rnd = ThreadLocalRandom.current();
        for (int i = ar.length - 1; i > 0; i--) {
            int index = rnd.nextInt(i + 1);
            int[] a = ar[index];
            ar[index] = ar[i];
            ar[i] = a;
        }
    }

    private void getProblem() {
        getValidBoard(false);
        int[][] pairs = new int[41][41];
        int counter1 = 0;
        int counter2 = 80;
        for (int i = 0; i < 40; i++) {
            pairs[i] = new int[]{counter1, counter2};
            counter1++;
            counter2--;
        }
        shuffleArray(pairs);
        for (int[] ints : pairs) {
            int i = ints[0];
            int j = ints[1];
            int temp1 = grid[Math.floorDiv(i, 9)][i % 9];
            int temp2 = grid[Math.floorDiv(j, 9)][j % 9];
            grid[Math.floorDiv(i, 9)][i % 9] = 0;
            grid[Math.floorDiv(j, 9)][j % 9] = 0;
            if (!solve(false)) {
                grid[Math.floorDiv(i, 9)][i % 9] = temp1;
                grid[Math.floorDiv(j, 9)][j % 9] = temp2;
            }
        }

    }

    private int countZeros() {
        int numOfZeros = 0;
        for (int[] ints : grid) {
            for (int anInt : ints) {
                if (anInt == 0) {
                    numOfZeros++;
                }
            }
        }
        return numOfZeros;
    }

    private void solveAlgo(boolean display) {
        for (int y = 0; y < 9; y++) {
            for (int x = 0; x < 9; x++) {
                if (grid[y][x] == 0) {
                    for (int n = 1; n < 10; n++) {
                        if (possible(x, y, n)) {
                            grid[y][x] = n;
                            solveAlgo(display);
                            if (!unique && !searching) {
                                return;
                            }
                            grid[y][x] = 0;
                        }
                    }
                    return;
                }
            }
        }
        if (searching) {
            unique = true;
            searching = false;
            if (display) {
                display();
            }
        } else if (unique) {
            unique = false;
        }
    }

    public boolean solve(boolean display) {
        unique = false;
        searching = true;
        solveAlgo(display);
        return unique;
    }
    public void solve(){
        solve(true);
    }

    public void display() {
        String brk = "-------------------------";
        int i = 0;
        for (int[] ints : grid) {
            if (i++ % 3 == 0) {
                System.out.println(brk);
            }
            int j = 0;
            for (int anInt : ints) {
                if (j++ % 3 == 0) {
                    System.out.print("| ");
                }
                if (anInt == 0) {
                    System.out.print("  ");
                } else {
                    System.out.print(anInt + " ");
                }
            }
            System.out.print("|");
            System.out.println();
        }
        System.out.println(brk);
    }

    public void gen(boolean display) {
        getProblem();
        while (countZeros() < 40) {
            grid = new int[9][9];
            getProblem();
        }
        if (display) {
            display();
        }
    }
    public void gen() {
        gen(true);
    }
}