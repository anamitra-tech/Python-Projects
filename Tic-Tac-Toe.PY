def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(cell if cell != '' else ' ' for cell in row))
        print("-" * 9)
        
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0] + " wins!"
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i] + " wins!"
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0] + " wins!"
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2] + " wins!"
    if all(cell != '' for row in board for cell in row):
        return "It's a draw!"
    return None  # Game ongoing

def get_move(player, board):
    while True:
        try:
            move = input(f"{player}'s turn. Enter row and column (1-3, separated by space): ").split()
            if len(move) != 2:
                print("Enter two numbers!")
                continue
            row, col = int(move[0])-1, int(move[1])-1
            if row not in range(3) or col not in range(3):
                print("Invalid position! Must be 1, 2, or 3.")
                continue
            if board[row][col] != '':
                print("Cell already taken. Choose another.")
                continue
            return row, col
        except ValueError:
            print("Enter valid numbers!")

# Main game loop
def play_game():
    board = [['' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    while True:
        print_board(board)
        row, col = get_move(players[turn % 2], board)
        board[row][col] = players[turn % 2]
        turn += 1
        
        result = check_winner(board)
        if result:
            print_board(board)
            print("\nGame Over! " + result)
            break

play_game()
