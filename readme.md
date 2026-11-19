# Sudoku Solver

A Sudoku solver built using Python and NumPy that solves Sudoku puzzles using a recursive backtracking algorithm.

## Features

- Accepts a Sudoku puzzle as input (0 represents an empty cell).
- Validates numbers against rows, columns and 3×3 grids.
- Solves puzzles using recursion and backtracking.
- Displays the completed Sudoku board with row and column labels.

## Algorithm

The solver uses **Backtracking**:

1. Find an empty cell in the Sudoku board.
2. Try numbers from 1 to 9.
3. Check whether the number is valid in the row, column and 3×3 grid.
4. If valid, place the number and recursively attempt to solve the remaining board.
5. If the attempt fails, reset the cell and try another number.
6. Continue until the board is solved or no valid solution exists.

## Requirements

- Python 3.x
- NumPy

Install NumPy:

```bash
pip install numpy
```

## How to Run

```bash
python main.py
```

Enter the Sudoku puzzle as 9 lines of 9 digits. Use `0` for empty cells.

## Technologies Used

- Python
- NumPy

## Project

Built as a personal project to practice Python, NumPy, recursion and backtracking.
