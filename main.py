# tic tac toe

# make winning_positions a set / hashmap
winning_positions = [
        [1, 2, 3]
        ,[1, 4, 7]
        ,[1, 5, 9]
        ,[3, 6, 9]
        ,[7, 8, 9]
        ,[7, 5, 3]]

# board = '   |   |   \n-----------\n   |   |   \n-----------\n   |   |   '
# def showBoard(x_moves, y_moves):

x_moves = []
y_moves = []
i = 0

while True:
    move = int(input('type your move: '))

    # input 0 to debug
    if move == 0:
        print('x_moves: ', end='')
        print(x_moves)
        print('y_moves: ', end='')
        print(y_moves)

    if move in x_moves or move in y_moves:
        print('this block is not empty')
        continue

    print('debugging')
    print('i: ', end='')
    print(i)
    if i % 2 == 0:
        print('x move')
        x_moves.append(move)
    else:
        print('y move')
        y_moves.append(move)

    for winning_pos in winning_positions:
        x = y = 0
        for winning_num in winning_pos:
            if winning_num in y_moves:
                y += 1
            if winning_num in x_moves:
                x += 1
        if x == 3:
            print('x won')
            break
        if y == 3:
            print('y won')
            break

    
    i += 1
