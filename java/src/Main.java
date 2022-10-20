public class Main {
    public static void main(String[] args) {
        Sudoku s = new Sudoku();
        s.display();
        s.solve();
        s.gen();
        s.solve();
    }
}