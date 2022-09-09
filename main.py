import pygame
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
BACKGROUND_COLOR = (0, 210, 182)
LINE_COLOR = (0, 179, 155)
CIRCLE_COLOR = (255, 255, 255)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 10
CROSS_COLOR = (0, 0, 0)
BOARD_ROWS = 3
BOARD_COLUMNS = 3
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC_TAC_TOE")
SCREEN.fill(BACKGROUND_COLOR)


def draw_lines():
    pygame.draw.line(SCREEN, LINE_COLOR, (195, 15), (195, 585), 10)
    pygame.draw.line(SCREEN, LINE_COLOR, (395, 15), (395, 585), 10)
    pygame.draw.line(SCREEN, LINE_COLOR, (15, 195), (585, 195), 10)
    pygame.draw.line(SCREEN, LINE_COLOR, (15, 395), (585, 395), 10)


BOARD = np.zeros((BOARD_ROWS, BOARD_COLUMNS))

draw_lines()


def draw_figures():
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            if BOARD[row][column] == 2:
                pygame.draw.circle(SCREEN, CIRCLE_COLOR, (int(column * 195 + 200 / 2), int(row * 200 + 195 / 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif BOARD[row][column] == 1:
                pygame.draw.line(SCREEN, CROSS_COLOR, (int(column * 200 + 35), int(row * 200 + 200-25)), (int(column * 200 + 200 - 45), int(row * 200 + 25)), CIRCLE_WIDTH)
                pygame.draw.line(SCREEN, CROSS_COLOR, (int(column * 200 + 35), int(row * 200 + 25)), (int(column * 200 + 200 - 45), int(row * 200 + 200 - 25)),CIRCLE_WIDTH)


def mark_square(row, column, player):
    BOARD[row][column] = player


def available_square(row, column):
    if BOARD[row][column] == 0:
        return True
    else:
        return False


def board_is_full():
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            if BOARD[row][column] == 0:
                return False
    return True


def check_win(player):
    for column in range(BOARD_COLUMNS):
        if BOARD[0][column] == player and BOARD[1][column] == player and BOARD[2][column] == player:
            draw_vertical_win_line(column, player)
            return True

    for row in range(BOARD_ROWS):
        if BOARD[row][0] == player and BOARD[row][1] == player and BOARD[row][2] == player:
            draw_horizonal_win_line(row, player)
            return True

    if BOARD[2][0] == player and BOARD[1][1] == player and BOARD[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if BOARD[0][0] == player and BOARD[1][1] == player and BOARD[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_win_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(SCREEN, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizonal_win_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(SCREEN, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(SCREEN, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(SCREEN, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    SCREEN.fill(BACKGROUND_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            BOARD[column][row] = 0


def main():
    player = 1
    game_over = False

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // 200)
                clicked_column = int(mouseX // 200)

                if available_square(clicked_row, clicked_column):
                    if player == 1:
                        mark_square(clicked_row, clicked_column, 1)
                        if check_win(player):
                            game_over = True
                        player = 2

                    elif player == 2:
                        mark_square(clicked_row, clicked_column, 2)
                        if check_win(player):
                            game_over = True
                        player = 1

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
                    game_over = False

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()