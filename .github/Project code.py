
import pygame
import sys

pygame.init()

#This sets up the board
Width, Height = 400, 400
Line_Width = 15
Board_rows, Board_cols = 3, 3
Square_size = Width // Board_cols
Circle_Radius = Square_size // 3
Circle_Width = 10
Cross_Width = 20
Space = Square_size // 4

#colors we are using in game
White = (255, 255, 255)
Black = (0, 0, 0)
Gray = (200, 200, 200)
Red = (255, 0, 0)
Blue = (0, 0, 255)

# sets up display screen
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(White)


board = [[0] * Board_cols for _ in range(Board_rows)]

#draw board
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, Black, (0, Square_size), (Width, Square_size),Line_Width)
    pygame.draw.line(screen, Black, (0, 2 * Square_size), (Width, 2 * Square_size),Line_Width)
    # Vertical lines
    pygame.draw.line(screen, Black, (Square_size, 0), (Square_size, Height), Line_Width)
    pygame.draw.line(screen, Black, (2 * Square_size, 0), (2 * Square_size, Height), Line_Width)

#draw figures/game pieces
def draw_figures():
    for row in range(Board_rows):
        for col in range(Board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, Red, (col * Square_size + Square_size // 2, row * Square_size + Square_size // 2), Circle_Radius, Circle_Width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, Blue, (col * Square_size + Space, row * Square_size + Square_size - Space), (col * Square_size + Square_size - Space, row * Square_size + Space), Cross_Width)
                pygame.draw.line(screen, Blue, (col * Square_size + Space, row * Square_size + Space), (col * Square_size + Square_size - Space, row * Square_size + Square_size - Space), Cross_Width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(Board_rows):
        for col in range(Board_cols):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    # Check rows
    for row in range(Board_rows):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # Check columns
    for col in range(Board_cols):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def restart_game():
    screen.fill(White)
    draw_lines()
    for row in range(Board_rows):
        for col in range(Board_cols):
            board[row][col] = 0

# Main game loop
player = 1
game_over = False

draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // Square_size
            clicked_col = mouseX // Square_size

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                    pygame.display.set_caption("Player " + str(player) + " wins!")
                elif is_board_full():
                    game_over = True
                    pygame.display.set_caption("It's a tie!")
                else:
                    player = 2 if player == 1 else 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                restart_game()
                player = 1
                pygame.display.set_caption("Tic Tac Toe")


    def check_win(player):
        for row in range(Board_rows):
            if board[row][0] == board[row][1] == board[row][2] == player:
                pygame.draw.line(screen, Red if player == 1 else Blue,
                                 (0, (row + 0.5) * Square_size),
                                 (Width, (row + 0.5) * Square_size),
                                 Line_Width)
                return True, (0, (row + 0.5) * Square_size, Width, (row + 0.5) * Square_size)

        for col in range(Board_cols):
            if board[0][col] == board[1][col] == board[2][col] == player:
                pygame.draw.line(screen, Red if player == 1 else Blue,
                                 ((col + 0.5) * Square_size, 0),
                                 ((col + 0.5) * Square_size, Height),
                                 Line_Width)
                return True, ((col + 0.5) * Square_size, 0, (col + 0.5) * Square_size, Height)

        if board[0][0] == board[1][1] == board[2][2] == player:
            pygame.draw.line(screen, Red if player == 1 else Blue,
                             (0, 0),
                             (Width, Height),
                             Line_Width)
            return True, (0, 0, Width, Height)
        if board[0][2] == board[1][1] == board[2][0] == player:
            pygame.draw.line(screen, Red if player == 1 else Blue,
                             (0, Height),
                             (Width, 0),
                             Line_Width)
            return True, (0, Height, Width, 0)
        return False, None



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // Square_size
                clicked_col = mouseX // Square_size

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    win, line_coords = check_win(player)
                    if win:
                        game_over = True
                        pygame.display.set_caption("Player " + str(player) + " wins!")
                        pygame.draw.line(screen, Red if player == 1 else Blue,
                                         line_coords[0:2], line_coords[2:4],
                                         Line_Width)
                    elif is_board_full():
                        game_over = True
                        pygame.display.set_caption("It's a tie!")
                    else:
                        player = 2 if player == 1 else 1

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                    restart_game()
                    player = 1
                    pygame.display.set_caption("Tic Tac Toe")


        pygame.display.update()