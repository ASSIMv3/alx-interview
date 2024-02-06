#!/usr/bin/python3
"""solves the N queens problem"""
import sys


def main() -> None:
    """Main function to solve the problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    columns = set()
    positive_diagonal = set()
    negative_diagonal = set()
    board = []

    def backtrack(row: int) -> None:
        """Recursive function to explore all possible queen placements"""
        if row == N:
            print(board)
            return

        for col in range(N):
            unvalid_col = col in columns
            unvalid_pos = (row + col) in positive_diagonal
            unvalid_neg = (row - col) in negative_diagonal
            if unvalid_col or unvalid_pos or unvalid_neg:
                continue

            columns.add(col)
            positive_diagonal.add(row + col)
            negative_diagonal.add(row - col)
            board.append([row, col])

            backtrack(row + 1)

            columns.remove(col)
            positive_diagonal.remove(row + col)
            negative_diagonal.remove(row - col)
            board.remove([row, col])

    backtrack(0)


if __name__ == '__main__':
    main()