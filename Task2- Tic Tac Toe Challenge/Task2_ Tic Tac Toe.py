print("=" * 40)
print("SMART TIC TAC TOE CHALLENGE")
print(" Human vs Computer")
print("=" * 40)
import random

board = [" " for _ in range(9)]

def print_positions():
    print("\nPositions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9\n")

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True

    return False

def is_full():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter your position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Choose a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("Position already occupied.")
                continue

            board[move] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")

def ai_move():
    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    move = random.choice(empty_positions)

    board[move] = "O"

    print("AI chose position", move + 1)

def play_game():

    print("=" * 35)
    print("TIC TAC TOE AI")
    print("=" * 35)

    print_positions()

    while True:

        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("Excellent Move! You Defeated The Computer.!")
            break

        if is_full():
            print_board()
            print("Match Draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("AI Wins!")
            break

        if is_full():
            print_board()
            print("Match Draw!")
            break

while True:

    board = [" " for _ in range(9)]

    play_game()

    again = input("\nPlay Again? (y/n): ")

    if again.lower() != "y":
        print("Thanks for Playing!")
        break
