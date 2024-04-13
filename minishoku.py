import random
"""
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
class Sudoku:
    def __init__(self):
        self.initialize_grid()
        self.fill_diagonal_subgrids()

    def initialize_grid(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        
    # Fist case of the grid and numbers for diagonal 
    def fill_diagonal_subgrids(self):
        numbers = list(range(1,10))
        for i in range(0, 9, 3):
            self.fill_grid(i, i, numbers) # (i,i) is the position where we start to fill the diagonal

def fill_grid(self, row, col, numbers):
        random.shuffle(numbers)
        for i in range(3):
            for j in range(3):
                self.grid[row + i][col + j] = numbers.pop(0)

sudoku = Sudoku()
for row in sudoku.grid:
    print(row)
    
    