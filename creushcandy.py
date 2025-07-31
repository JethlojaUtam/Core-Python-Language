import random
import os

# --- Game Configuration ---
BOARD_WIDTH = 8
BOARD_HEIGHT = 8
CANDY_TYPES = ['A', 'B', 'C', 'D', 'E', 'F']
SCORE_PER_MATCH = 10
MOVES_LIMIT = 30

def create_board():
    """Creates a new game board with random candies."""
    return [[random.choice(CANDY_TYPES) for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board(board, score, moves_left):
    """Prints the current state of the game board and stats."""
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the console
    print("--- Welcome to Candy Match! ---")
    print(f"Score: {score} | Moves Left: {moves_left}")
    print("-" * (BOARD_WIDTH * 3 + 5))
    
    # Print column headers
    print("   ", end="")
    for i in range(BOARD_WIDTH):
        print(f" {i} ", end="")
    print("\n  " + "-" * (BOARD_WIDTH * 3))

    # Print rows with headers
    for r_idx, row in enumerate(board):
        print(f"{r_idx} |", end="")
        for candy in row:
            print(f" {candy} ", end="")
        print("|")
    print("-" * (BOARD_WIDTH * 3 + 5))

def is_valid_swap(r1, c1, r2, c2):
    """Checks if a swap is valid (adjacent candies)."""
    return abs(r1 - r2) + abs(c1 - c2) == 1

def find_matches(board):
    """Finds all horizontal and vertical matches of 3 or more."""
    matches = set()
    # Horizontal matches
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH - 2):
            if board[r][c] == board[r][c+1] == board[r][c+2] and board[r][c] is not None:
                matches.add((r, c))
                matches.add((r, c+1))
                matches.add((r, c+2))
    
    # Vertical matches
    for c in range(BOARD_WIDTH):
        for r in range(BOARD_HEIGHT - 2):
            if board[r][c] == board[r+1][c] == board[r+2][c] and board[r][c] is not None:
                matches.add((r, c))
                matches.add((r+1, c))
                matches.add((r+2, c))
    return list(matches)

def remove_matches(board, matches):
    """Removes matched candies from the board (sets them to None)."""
    for r, c in matches:
        board[r][c] = None
    return len(matches) * SCORE_PER_MATCH

def drop_candies(board):
    """Drops candies down to fill empty spaces."""
    for c in range(BOARD_WIDTH):
        empty_spaces = 0
        for r in range(BOARD_HEIGHT - 1, -1, -1):
            if board[r][c] is None:
                empty_spaces += 1
            elif empty_spaces > 0:
                board[r + empty_spaces][c] = board[r][c]
                board[r][c] = None

def refill_board(board):
    """Refills the top of the board with new random candies."""
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if board[r][c] is None:
                board[r][c] = random.choice(CANDY_TYPES)

def get_player_input():
    """Gets and validates the player's input for a swap."""
    while True:
        try:
            prompt = "Enter your swap (row1,col1 row2,col2), e.g., '4,2 4,3': "
            move_input = input(prompt)
            parts = move_input.split()
            if len(parts) != 2:
                raise ValueError("Invalid format.")
            
            r1, c1 = map(int, parts[0].split(','))
            r2, c2 = map(int, parts[1].split(','))

            if 0 <= r1 < BOARD_HEIGHT and 0 <= c1 < BOARD_WIDTH and \
               0 <= r2 < BOARD_HEIGHT and 0 <= c2 < BOARD_WIDTH:
                return r1, c1, r2, c2
            else:
                print("Coordinates are out of bounds. Try again.")

        except (ValueError, IndexError):
            print("Invalid input. Please use the format 'row,col row,col'.")

def candy_match_game():
    """Main function to run the Candy Match game."""
    board = create_board()
    score = 0
    moves_left = MOVES_LIMIT

    # Initial cascade to ensure no starting matches
    while True:
        matches = find_matches(board)
        if not matches:
            break
        remove_matches(board, matches)
        drop_candies(board)
        refill_board(board)

    while moves_left > 0:
        print_board(board, score, moves_left)
        
        r1, c1, r2, c2 = get_player_input()

        if not is_valid_swap(r1, c1, r2, c2):
            print("\nInvalid swap! Candies must be adjacent. Try again.")
            input("Press Enter to continue...")
            continue

        # Perform the swap
        board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]
        
        total_score_from_move = 0
        
        # Check for matches in a loop to handle cascades
        while True:
            matches = find_matches(board)
            if not matches:
                # If no matches, swap back and penalize the move.
                if total_score_from_move == 0:
                    print("\nNo match found with that swap. Reverting.")
                    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]
                break
            
            total_score_from_move += remove_matches(board, matches)
            
            # Animate the drop/refill
            time.sleep(0.5)
            print_board(board, score, moves_left)
            
            time.sleep(0.5)
            drop_candies(board)
            print_board(board, score, moves_left)

            time.sleep(0.5)
            refill_board(board)
            print_board(board, score, moves_left)

        if total_score_from_move > 0:
            score += total_score_from_move
        
        moves_left -= 1
        input("\nPress Enter for the next turn...")

    # Game Over
    print_board(board, score, moves_left)
    print("\n--- GAME OVER! ---")
    print(f"Your final score is: {score}")

# --- Main execution block ---
if __name__ == "__main__":
    candy_match_game()
