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
            return board

    board[len(board) - 1][col] = piece
    return board        
                

def isWin(board, col, row):
    # Check if there is a win and return true of false

    return True

def main():
    board =[[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]


    #Each player takes turns
    #If there is a win end game 
    #if board is full end game
    

main()