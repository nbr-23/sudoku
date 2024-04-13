import random

class Sudoku:
    def __init__(self):
        self.initialize_grid()
        self.fill_diagonal_subgrids()

    def initialize_grid(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        
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
    # Starting with siagonal subgrids is a common strategy in Sudoku generation algorithms to ensure uniqueness of solution.
    def fill_diagonal_subgrids(self):
        for i in range(0, 9, 3):
            self.fill_grid(i, i)

    """
    [4, 2, 9, 0, 0, 0, 0, 0, 0]
    [8, 6, 5, 0, 0, 0, 0, 0, 0]
    [7, 1, 3, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 1, 9, 4, 0, 0, 0]
    [0, 0, 0, 6, 3, 7, 0, 0, 0]
    [0, 0, 0, 2, 8, 5, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 4, 6, 5]
    [0, 0, 0, 0, 0, 0, 1, 9, 2]
    [0, 0, 0, 0, 0, 0, 8, 7, 3]
    """
    def fill_grid(self, row, col):
        numbers = random.sample(range(1, 10), 9)
        index = 0
        for i in range(3):
            for j in range(3):
                self.grid[row + i][col + j] = numbers[index]
                index += 1

    """
    [9, 3, 2, 1, 1, 1, 1, 1, 1]
    [1, 4, 8, 1, 1, 1, 1, 1, 1]
    [7, 6, 5, 1, 1, 1, 1, 1, 1]
    [1, 1, 1, 6, 4, 5, 1, 1, 1]
    [1, 1, 1, 1, 8, 2, 1, 1, 1]
    [1, 1, 1, 9, 3, 7, 1, 1, 1]
    [1, 1, 1, 1, 1, 1, 7, 4, 2]
    [1, 1, 1, 1, 1, 1, 5, 9, 8]
    [1, 1, 1, 1, 1, 1, 3, 6, 1]
    """
    def solve_sudoku(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        # Function to check if valid number => if valid_number ..
                        self.grid[row][col] = num
                        if self.solve_sudoku():
                            return True
                        self.grid[row][col] = 0
                    return False
        return True
    
        
    # Create a function ro check if the number is valid 
    # Create a function to remove some random numbers 
    # Part one done ===
    
    #Part two add PyGame
    
sudoku = Sudoku()


solution_found = sudoku.solve_sudoku()


if solution_found:
    print("Sudoku solved ! ")
    for row in sudoku.grid:
        print(row)
else:
    print("Not solved..")