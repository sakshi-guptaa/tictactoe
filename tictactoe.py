import os

board=[['1','2','3'],['4','5','6'],['7','8','9']]

#Display gameboard
def gameboard(board):
    print (" ---" * 3)
    print ("| "+ board[0][0]+" | "+ board[0][1]+" | "+ board[0][2]+" |")
    print (" ---" * 3)
    print ("| "+ board[1][0]+" | "+ board[1][1]+" | "+ board[1][2]+" |")
    print (" ---" * 3)
    print ("| "+ board[2][0]+" | "+ board[2][1]+" | "+ board[2][2]+" |")
    print (" ---" * 3)

#Finding the row and column number from the index entered by the user
def find_pos(X):
    pos=[0,0]
    pos[0] = X // 3
    pos[1] = X % 3
    if pos[1] == 0:
        pos[0] -= 1
        pos[1] = 2
    else:
        pos[1] -= 1
    return pos

#Check if there is a winner before going for the next turn
def check_winner(board):
    #for rows
    for i in range (0,3):
        row= set([board[i][0],board[i][1],board[i][2]])
        if len(row)==1:
            return board[i][0]

    #for columns
    for i in range (0,3):
        col= set([board[0][i],board[1][i],board[2][i]])
        if len(col)==1:
            return board[0][i]

    # diagonals
    if board[1][1] == board[0][0] == board[2][2]:
        return board[1][1]
    elif board[1][1] == board[0][2] == board[2][0]:
        return board[1][1]

    return 0


#Inserting 'X' or 'O' on the board
def insert_on_board(board,pos,playernum):
    if board[pos[0]][pos[1]]!='X' or board[pos[0]][pos[1]]!='O':
        if playernum==1:
            board[pos[0]][pos[1]]='X'
        elif playernum==2:
            board[pos[0]][pos[1]]='O'


#main function
os.system('cls')
player1= input("What is your name, player 1?: ")
player2= input("What is your name, player 2?: ")

os.system('cls')

gameboard(board)
cnt=9

while cnt>0:
    num= int(input(player1 + ", where would you like to place 'X'? : "))
    if num<0 or num>9:
        print("Invalid number entered")
    else:
        pos= find_pos(num)
        insert_on_board(board,pos,1)
        cnt-=1
        os.system('cls')
        gameboard(board)

        ans=check_winner(board)
        if ans=='X':
            print(player1 + " won!!")
            break
        elif ans=='O':
            print(player2 + " won!!")
            break

    if cnt==0:
        print("game draw!!")
        break

    num = int(input(player2 + ", where would you like to place 'O'? : "))
    if num < 0 or num > 9:
        print("Invalid number entered")
    else:
        pos = find_pos(num)
        insert_on_board(board,pos,2)
        cnt-=1
        os.system('cls')
        gameboard(board)

        ans = check_winner(board)
        if ans == 'X':
            print(player1 + " won!!")
            break
        elif ans == 'O':
            print(player2 + " won!!")
            break
    if cnt==1:
        print("game draw!!")
        break



