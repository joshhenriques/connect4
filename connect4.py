def printBoard(board):

    print('\n---------------')
    for i in range(len(board)):
        print('|' , end ='')
        for j in range(len(board[0])):
            print(str(board[i][j]) + '|' , end ='')

        print('\n---------------')

def placePiece(board, piece):
    while True:
        col= input("\nWhich column would you like to place the piece in: ")
        try:
            col = int(col)
            col -= 1
            if board[0][col] != 0:
                print("Column is full, please select a different one") 
            elif col >= 1 or col <= 7:
                break
            else: 
                print("\nMust be a column from 1 and 7")
        except:
            print("Enter a number from 1 to 7")
            pass
    

    for i in range(1,len(board)):
        if board[i][col] != 0:
            board[i-1][col] = piece
            print(isWin(board, i-1, col))
            return board

    board[len(board) - 1][col] = piece
    print(isWin(board, len(board) - 1, col))
    return board       
                

def isWin(board, row, col):
    # Check if there is a win and return true of false
    piece = board[row][col]
    ver = 0
    hor = 0
    rDiag = 0
    lDiag = 0

    r = True
    l = True
    u = True
    d = True
    ur = True
    ul = True
    dr = True
    dl = True

    print(len(board))
    for i in range(1,5):

        if col + i >= len(board[0]): #checks if on right edge
            r = False
            ur = False
            dr = False
        if col - i < 0: #checks if on left edge
            l = False
            ul = False
            dl = False
        if row - i < 0: #checks if on top edge
            u = False
            ur = False
            ul = False
        if row + i >= len(board): #checks if on bottom edge
            d = False
            dr = False
            dl = False

        #Checks right
        if r:
            if board[row][col + i] == piece:
                hor += 1
            else:
                r = False

        #Checks Left
        if l:
            if board[row][col - i] == piece:
                hor += 1
            else:
                l = False

        #Checks Up
        if u:
            if board[row - i][col] == piece:
                ver += 1
            else:
                u = False

        #Checks Down
        if d:
            if board[row + i][col] == piece:
                ver += 1
            else:
                d = False

        #Checks Up right
        if ur:
            if board[row - i][col + i] == piece:
                rDiag += 1
            else:
                ur = False

        #Checks down left
        if dl:
            if board[row + i][col - i] == piece:
                rDiag += 1
            else:
                dl = False

        #Checks up left
        if ul:
            if board[row - i][col - i] == piece:
                lDiag += 1
            else:
                ul = False

        #Checks down right
        if dr:
            if board[row + i][col + i] == piece:
                lDiag += 1
            else:
                dr = False

    return (hor == 3) or (ver == 3) or (rDiag == 3) or (lDiag == 3)

def main():
    board =[[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,2,0,2,1,0,0],
            [0,2,2,1,1,0,0],
            [0,2,1,2,1,1,0]]


    placePiece(board, 2)
    
    #Each player takes turns
    #If there is a win end game 
    #if board is full end game
    

main()