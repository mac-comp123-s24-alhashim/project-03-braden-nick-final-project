
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
Width, Height = 400, 400
Line_Width = 15
Board_rows, Board_cols = 3, 3
Square_size = Width // Board_cols
Circle_Radius = Square_size // 3
Circle_Width = 10
Cross_Width = 20
Space = Square_size // 4

# Colors
White = (255, 255, 255)
Black = (0, 0, 0)
Gray = (200, 200, 200)
Red = (255, 0, 0)
Blue = (0, 0, 255)

# Display
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(White)

# Board
board = [[0] * Board_cols for _ in range(Board_rows)]
