import random
import sys
import pygame

class Sudoku:
    def __init__(self):
        self.initialize_grid()
        self.fill_diagonal_subgrids()
        self.selected_cell = None

    def initialize_grid(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        
    def fill_diagonal_subgrids(self):
        for i in range(0, 9, 3):
            self.fill_grid(i, i)

    def fill_grid(self, row, col):
        numbers = random.sample(range(1, 10), 9)
        index = 0
        for i in range(3):
            for j in range(3):
                self.grid[row + i][col + j] = numbers[index]
                index += 1
                
    def is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num:
                return False
        for i in range(9):
            if self.grid[i][col]== num:
                return False
                
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
    
    def remove_numbers(self, num_to_remove):
        for _ in range(num_to_remove):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.grid[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            self.grid[row][col] = 0
            
    def draw_grid(self, screen):
            cell_size = 540 // 9
            font = pygame.font.Font(None, 36)
            for row in range(9):
                for col in range(9):
                    x = col * cell_size
                    y = row * cell_size
                    rect = pygame.Rect(x, y, cell_size, cell_size)
                    pygame.draw.rect(screen, (255, 255, 255), rect)  # Draw white cell
                    pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Draw cell border
                    if self.selected_cell == (row, col):  # Highlight selected cell
                        pygame.draw.rect(screen, (200, 255, 200), rect, 3)
                    if self.grid[row][col] != 0:
                        text = font.render(str(self.grid[row][col]), True, (0, 0, 0))
                        text_rect = text.get_rect(center=rect.center)
                        screen.blit(text, text_rect)
                        
    def handle_mouse_click(self, pos):
        cell_size = 540 // 9
        row = pos[1] // cell_size
        col = pos[0] // cell_size
        self.selected_cell = (row, col)

    def handle_keypress(self, key):
        if self.selected_cell:
            row, col = self.selected_cell
            if pygame.K_1 <= key <= pygame.K_9:
                num = key - pygame.K_1 + 1
                if self.is_valid(row, col, num):
                    self.grid[row][col] = num
            elif key == pygame.K_DELETE or key == pygame.K_BACKSPACE:
                self.grid[row][col] = 0
                        
  
            
# Initialise Pygame
pygame.init()

# Create an instance of Sudoku
sudoku = Sudoku()

# Solve Sudoku
solution_found = sudoku.solve_sudoku()

if solution_found:
    sudoku.remove_numbers(40)
    print("Sudoku puzzle:")
    for row in sudoku.grid:
        print(row)
else:
    print("Unable to solve Sudoku.")

# Initialise Pygame window
WINDOW_SIZE = [540, 540]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        
        
            
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse clicks
            sudoku.handle_mouse_click(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:  # Handle keypresses
            sudoku.handle_keypress(event.key)
            

    screen.fill((255,255,255))
    sudoku.draw_grid(screen)
    pygame.display.flip()

    clock.tick(30)
    
pygame.quit()
sys.exit()
