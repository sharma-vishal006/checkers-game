
import pygame
from checkers.constants import SQUARE_SIZE, WIDTH,HEIGHT
from checkers.board import Board
from checkers.piece import Piece
from checkers.game import Game

FPS=60
WIN=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Checkers Game')


def get_row_col_from_mouse(pos):
    x, y = pos
    row=y // SQUARE_SIZE
    col= x // SQUARE_SIZE
    print("Hello Vishal")
    return row,col

def main():
    run= True
    clock=pygame.time.Clock()
    game=Game(WIN)

    # piece=board.get_piece(0,1)
    # board.move(piece,4,3)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Hello")
                run=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                row,col=get_row_col_from_mouse(pos)
                # piece=board.get_piece(row,col)
                # board.move(piece,4,3)
                # if game.turn ==RED:
                

                game.select(row,col)


        game.update ()        
    pygame.quit()


main()
