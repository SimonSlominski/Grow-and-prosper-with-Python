# TIC TAC TOE Game
# The player is playing a game against a computer

# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def instructions():
    """
    Display game instructions
    """

    print(
    """
    It's a pleasure to welcome you in a 'Tic-tac-toe' game!
    
    
    This is the instructions for the game:  

    You will indicate your move by entering a number between 1 and 9.
    This number corresponds to the position on the board according to the following diagram:

                    1 | 2 | 3
                    ---------
                    4 | 5 | 6
                    ---------
                    7 | 8 | 9

    Get ready to play! \n
    """
    )


def ask_yes_no(question):
    """
    Ask a question that you can answer yes or no.
    """
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """
    Ask for a number from the appropriate range
    """
    response = None
    while response not in range(low, high):
        # -1 is to allow you to play 1-9 square board
        # Without '-1' you have to choose square from 0 to 8 what is missleading
        response = int(input(question))-1
    return response


def move_order():
    """
    Determine if the first move belongs to the player or to the computer.
    """
    go_first = ask_yes_no('Do you want to be entitled to make the first move? (y/n): ')

    if go_first == 'y':
        print('\nThe first move is yours')
        player = X
        computer = O
    else:
        print('\nThe first move will be done by the computer')
        computer = X
        player = O
    return computer, player


def new_board():
    """
    Create a new board for the game
    """
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """
    Display the board on the screen
    """
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_move(board):
    """
    Creates a list of available moves
    """
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """
    Determine the winner of the game
    """
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def player_move(board, player):
    """
    Reads the player's move
    """

    legal = legal_move(board)
    move = None

    while move not in legal:
        move = ask_number("What's your move (1 - 9)", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThis square is already taken. Choose available square\n")
    print('Exellent')
    return move


def computer_move(board, computer, player):
    """
    Makes the computer move.
    """

    # create a working copy because the function will change the list
    board = board[:]

    # best moves to take in the order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print('I choose the square number:', end=' ')

    # if the computer can win, make this move
    for move in legal_move(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # this move has been checked, retract it
        board[move] = EMPTY

    # if the player can win, block this move
    for move in legal_move(board):
        board[move] = player
        if winner(board) == player:
            print(move)
            return move
        # this move has been checked, retract it
        board[move] = EMPTY

    # because no one can win in the next move, choose the best free square
    for move in BEST_MOVES:
        if move in legal_move(board):
            print(move)
            return move


def next_turn(turn):
    """
    Changes the side that makes the move
    """
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, player):
    """
    Congratulate the winner
    """

    if the_winner != TIE:
        print(the_winner, 'win the game!\n')
    else:
        print('Tie!\n')

    if the_winner == computer:
        print('Man can not equal to the machine!')

    if the_winner == player:
        print('Congratulation. You have won a battle against the machines!')

    if the_winner == TIE:
        print('An unresolved duel. Try again')


def main():
    instructions()
    computer, player = move_order()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == player:
            move = player_move(board, player)
            board[move] = player
        else:
            move = computer_move(board, computer, player)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, player)

main()
input("\n\n To end this game, press Enter")

