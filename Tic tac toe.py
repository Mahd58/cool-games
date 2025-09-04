# Write a Python Program to create a Tic Tac Toe game. You can use different modules and functions to create this game. Make sure that you print the board after every move.
board={
    "7":" ","8":" ","9":" ",
    "4":" ","5":" ","6":" ",
    "1":" ","2":" ","3":" ",
}
board_keys=[i for i in board.keys()]
def print_board(board):
    print(board["7"]+"|"+board["8"]+"|"+board["9"]+"|")
    print(board["4"]+"|"+board["5"]+"|"+board["6"]+"|")
    print(board["1"]+"|"+board["2"]+"|"+board["3"]+"|")
print_board(board)
def game():
    turn="X"
    count=0
    for i in range(0,10):
        print("This is your board")
        print_board(board)
        print("Enter the place where you want it to move your ",turn)
        move=input()
        if board[move]==" ":
            board[move]=turn
            count=count+1
        else:
            print("this place is already filled!")
            continue
        if count>=5:
            if board["7"]==board["8"]==board["9"]!=" ":
                print_board(board)
                print("game over")
                print(turn," you win the game")
                break
            elif board["4"]==board["5"]==board["6"]!=" ":
                print_board(board)
                print("game over")
                print(turn," you win the game")
                break
            elif board["1"]==board["2"]==board["3"]!=" ":
                print_board(board)
                print("game over")
                print(turn," you win the game")
                break
            elif board["1"]==board["4"]==board["7"]!=" ":
                print_board(board)
                print("game over")
                print(turn," you win the game")
                break
            elif board["8"]==board["5"]==board["2"]!=" ":
                print_board(board)
                print("game over")
                print(turn," you win the game")
                break
            elif board["9"]==board["6"]==board["3"]!=" ":
                print_board(board)
                print("game over")
                print(turn," you win the game")
                break
            elif board["1"]==board["5"]==board["9"]!=" ":
                print_board(board)
                print("game over")
                print(turn," you win the game")
                break
            elif board["3"]==board["5"]==board["7"]!=" ":
                print_board(board)
                print("game over")
                print(turn," you win the game")
                break
        if count==9:
            print("Congragulations its a draw!")
        if turn=="X":
            turn="0"
        else:
            turn="X"
game()