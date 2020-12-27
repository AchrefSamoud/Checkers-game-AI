import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
import pygame_menu

GAMEMODE=1
DEPTH = 1
FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE and GAMEMODE==1:
            value, new_board = minimax(game.get_board(), DEPTH, WHITE, game)
            game.ai_move(new_board)

        if game.turn == WHITE and GAMEMODE==2:
             if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    value, new_board = minimax(game.get_board(), DEPTH, 0, game)
                    game.ai_move(new_board)

        game.update()
    
    menu.mainloop(WIN)

def set_difficulty(val, dif):
    global DEPTH
    if dif == 1:
        DEPTH = 5
    else:
        DEPTH = 1
    pass
def set_game(val,dif):
    global GAMEMODE
    if dif==1:
        GAMEMODE=1
    else:
        GAMEMODE=2    



menu = pygame_menu.Menu(300, 400, 'Checkers', theme=pygame_menu.themes.THEME_DARK)
menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_selector('PLAY AGAINST :', [('AI', 1), ('HUMAN', 2)], onchange=set_game)

menu.add_button('Play', main)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(WIN)