def printBoard(board):

    print('\n---------------')
    for i in range(len(board)):
        print('|' , end ='')
        for j in range(len(board[0])):
            print(str(board[i][j]) + '|' , end ='')

        print('\n---------------')

board =[[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]

printBoard(board)
        