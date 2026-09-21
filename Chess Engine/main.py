
# Joshua LR 19/9/26
# Chess Game with PyGame

import pygame as py
import time
from data import Chessboard

WIDTH = HEIGHT = 800
SQUAREDIMENSIONS = int(WIDTH/8) # Width and height of a square


py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
gameBoard = Chessboard()


# Save images in a dictionary
pieces = ['wr', 'wn', 'wb', 'wq', 'wk', 'wp', 'br', 'bn', 'bb', 'bq', 'bk', 'bp']
imageDict = {}
for piece in pieces:
    name = (f'images/{piece}.png')
    baseImage = py.image.load(name)
    imageDict[piece] = py.transform.smoothscale(baseImage, (SQUAREDIMENSIONS, SQUAREDIMENSIONS))
    # Smoothscale is more computationally expensive but has smoother edges (better)


# Draw alternating coloured squares
def drawSquares(screen):
    for y in range(0, HEIGHT, SQUAREDIMENSIONS):
        for x in range(0, WIDTH, SQUAREDIMENSIONS):

            if ((x / SQUAREDIMENSIONS) + (y / SQUAREDIMENSIONS)) % 2 == 0: # Even number = white
                colour = (255,255,255)
            else: # Odd number = black
                colour = (100,100,100)

            py.draw.rect(screen, colour, (x, y, SQUAREDIMENSIONS, SQUAREDIMENSIONS))


# Draw chess pieces
def drawPieces(screen, board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != '--':
                screen.blit(imageDict[(board[row][col])], (col*SQUAREDIMENSIONS, row*SQUAREDIMENSIONS))


def selectPiece(mousePos):
    col = mousePos[0] // SQUAREDIMENSIONS
    row = mousePos[1] // SQUAREDIMENSIONS

    return [row, col]


# Move piece at square1 to square2
def movePieces(board, square1, square2): 
    board[square2[0]][square2[1]] = board[square1[0]][square1[1]]
    board[square1[0]][square1[1]] = '--'


# Main game loop
running = True
selectedSquare = []
while running:
    drawSquares(screen)
    drawPieces(screen, gameBoard.board)
    py.display.flip()
    
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            mousePos = py.mouse.get_pos()
            if selectedSquare: # If previous square already selected
                temporarySquare = selectPiece(mousePos)
                if temporarySquare and temporarySquare != selectedSquare: # Not empty or same square
                    previousSquare = selectedSquare
                    selectedSquare = temporarySquare
                    movePieces(gameBoard.board, previousSquare, selectedSquare)
                    selectedSquare = [] # Reset selected square so a new piece can be selected
            else:
                temporarySquare = selectPiece(mousePos)
                if gameBoard.board[temporarySquare[0]][temporarySquare[1]] != '--':
                    selectedSquare = temporarySquare

    

















