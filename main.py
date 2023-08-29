# tic tac toe

import os
from time import sleep

print('Welcome to Tic Tac Toe!')
print('This is how you play: ')
print(' 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 ')
print('Press the value corresponding to the position you want to place your mark')

input('Press any key to start: ')

os.system('clear')

win_positions = [
         [1, 2, 3]
        ,[4, 5, 6]
        ,[7, 8, 9]

        ,[1, 4, 7]
        ,[2, 5, 8]
        ,[3, 6, 9]

        ,[1, 5, 9]
        ,[7, 5, 3]]

def showBoard(x_moves, o_moves, finalResult = False):
    pos1 = 'X' if 1 in  x_moves else 'O' if 1 in o_moves else ' '
    pos2 = 'X' if 2 in  x_moves else 'O' if 2 in o_moves else ' '
    pos3 = 'X' if 3 in  x_moves else 'O' if 3 in o_moves else ' '
    pos4 = 'X' if 4 in  x_moves else 'O' if 4 in o_moves else ' '
    pos5 = 'X' if 5 in  x_moves else 'O' if 5 in o_moves else ' '
    pos6 = 'X' if 6 in  x_moves else 'O' if 6 in o_moves else ' '
    pos7 = 'X' if 7 in  x_moves else 'O' if 7 in o_moves else ' '
    pos8 = 'X' if 8 in  x_moves else 'O' if 8 in o_moves else ' '
    pos9 = 'X' if 9 in  x_moves else 'O' if 9 in o_moves else ' '

    if not finalResult:
        print('Current board              How to play\n {} | {} | {}                  7 | 8 | 9 \n-----------                -----------\n {} | {} | {}                  4 | 5 | 6 \n-----------                -----------\n {} | {} | {}                  1 | 2 | 3 '.format(pos7, pos8, pos9, pos4, pos5, pos6, pos1, pos2, pos3))
    else:
        print('Result\n {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} '.format(pos7, pos8, pos9, pos4, pos5, pos6, pos1, pos2, pos3))

x_moves = []
o_moves = []

isXturn = True
gameOn = True

while gameOn:
    showBoard(x_moves, o_moves)

    move = int(input('type your move: '))

    if move in x_moves or move in o_moves:
        print('Invalid move, try again')
        continue

    if isXturn:
        x_moves.append(move)
    else:
        o_moves.append(move)

    os.system('clear')

    for win_pos in win_positions:
        x = o = 0
        for win_num in win_pos:
            if win_num in x_moves:
                x += 1
            if win_num in o_moves:
                o += 1
        if x == 3 or o == 3:
            print('\033[32m{} wins!\033[m'.format('X' if x == 3 else 'O'))
            showBoard(x_moves, o_moves, True)
            input('Press any key to end the game: ')
            gameOn = False

    isXturn = not isXturn

