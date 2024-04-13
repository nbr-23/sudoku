import random
import sys
import pygame

pygame.init()

WINDOW_SIZE = [540, 540]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku")

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
                
    

    def is_valid(self, row, col, num):
        
        # Check if the number exists in the row
        for i in range(9):
            if self.grid[row][i] == num:
                return False
        # Check if the number exists in the column
        for i in range(9):
            if self.grid[i][col]== num:
                return False
                
        # Check if the number exists in the 3x3 grid 
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
                
        return True
        
    
    def solve_sudoku(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve_sudoku():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True
    
    
    """
    [8, 9, 0, 0, 0, 0, 0, 0, 7]
    [6, 5, 7, 3, 0, 9, 0, 0, 2]
    [1, 2, 4, 6, 5, 7, 0, 0, 3]
    [0, 0, 5, 9, 6, 0, 8, 0, 4]
    [0, 0, 0, 0, 4, 2, 0, 0, 0]
    [0, 6, 0, 0, 0, 8, 0, 0, 0]
    [5, 0, 2, 7, 9, 0, 4, 1, 8]
    [7, 0, 0, 8, 0, 0, 3, 0, 0]
    [9, 8, 0, 0, 0, 5, 7, 2, 6]
    """
    def remove_numbers(self, num_to_remove):
        for _ in range(num_to_remove):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.grid[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            self.grid[row][col] = 0
    

    
    
sudoku = Sudoku()

solution_found = sudoku.solve_sudoku()

if solution_found:
    sudoku.remove_numbers(40)  # Example: Remove 50 numbers to create a puzzle
    
    print("Sudoku puzzle:")
    for row in sudoku.grid:
        print(row)
else:
    print("Unable to solve Sudoku.")