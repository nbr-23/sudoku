# 1 = implement your game in such a way that it contains a game grid, as well as a generation of numbers on this grid. 

"""
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
"""
class Sudoku:
    def __init__(self):
        self.initialize_grid()

    def initialize_grid(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

# Example usage
sudoku = Sudoku()
print(sudoku.grid)
