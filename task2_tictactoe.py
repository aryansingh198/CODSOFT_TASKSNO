"""
CODSOFT - Artificial Intelligence Internship
TASK 2: TIC-TAC-TOE AI

An unbeatable Tic-Tac-Toe AI using the Minimax algorithm with
Alpha-Beta Pruning. Human plays 'X', AI plays 'O'.
"""

import math

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        print(" | ".join(row))
        if i < 6:
            print("-" * 9)
    print()


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def check_winner(board):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]
    for a, b, c in win_combos:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "DRAW"
    return None


def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif winner == "DRAW":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def best_ai_move(board):
    best_score = -math.inf
    move_choice = None
    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice


def play():
    board = [EMPTY] * 9
    print("Tic-Tac-Toe: You are 'X', AI is 'O'. Positions are numbered 0-8:")
    print_board([str(i) for i in range(9)])

    current = HUMAN
    while True:
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "DRAW":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        if current == HUMAN:
            try:
                move = int(input("Your move (0-8): "))
            except ValueError:
                print("Enter a number between 0-8.")
                continue
            if move not in available_moves(board):
                print("Invalid move, try again.")
                continue
            board[move] = HUMAN
            current = AI
        else:
            move = best_ai_move(board)
            board[move] = AI
            print(f"AI plays at position {move}")
            current = HUMAN

        print_board(board)


if __name__ == "__main__":
    play()
