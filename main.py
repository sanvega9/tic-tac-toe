def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def board_full(board):
    return all([spot != " " for row in board for spot in row])

def ai_move(board):
    # AI tries to win or block player's win
    for player in ["O", "X"]:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    if check_winner(board, player):
                        board[i][j] = "O"
                        return
                    board[i][j] = " "
    # Take center
    if board[1][1] == " ":
        board[1][1] = "O"
        return
    # Take corners
    for i, j in [(0,0), (0,2), (2,0), (2,2)]:
        if board[i][j] == " ":
            board[i][j] = "O"
            return
    # Take any available space
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                return

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Spot already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number 1-9.")

def main():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        if board_full(board):
            print("It's a draw!")
            break
        ai_move(board)
        print("AI moved:")
        print_board(board)
        if check_winner(board, "O"):
            print("AI wins! 😢")
            break
        if board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
