# Python Sudoku Generator and Solver

## Instructions

All functions belong to a Sudoku object.

When an instance of the class is created a Sudoku is generated.

To Create and object named 'x':

    x = Sudoku()

## Functions

`display()`

> Displays the grid.

`possible(x, y, n)`

> Returns bool wether n is valid in the grid at position x,y
>
> Pass in x as the column, y as the row, n as the number to check.

`getValidBoard(display=True)`

> Creates a full sudoku Board that is valid.
>
> Pass in the bool of displayed to determine wether the full board is displayed.

`solve(display=True)`

> This will solve the sudoku in the current grid.
>
> Pass in the bool of displayed to determine wether the solved board is displayed.

`getProblem(display=True)`

> Creates a valid sudoku problem.
>
> Pass in the bool of displayed to determine wether the solved board is displayed.

`gen(display=True)`

> Creates a valid sudoku problem with at least 30 missing values.
>
> Pass in the bool of displayed to determine wether the solved board is displayed.
