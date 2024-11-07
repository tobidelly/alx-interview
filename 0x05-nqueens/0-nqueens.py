#!/usr/bin/python3
""" N queens """
import sys

# Validate command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])

if n < 4:
    print("N must be at least 4")
    exit(1)

def queens(n, row=0, columns=[], diag1=[], diag2=[]):
    """ Generate valid queen positions row by row """
    if row == n:
        yield columns
    else:
        for col in range(n):
            if col not in columns and row + col not in diag1 and row - col not in diag2:
                # Place queen and proceed to next row
                yield from queens(n, row + 1, columns + [col], diag1 + [row + col], diag2 + [row - col])

def solve(n):
    """ Solve and print each solution """
    for solution in queens(n):
        # Format each solution to [[row, col], ...] and print it
        formatted_solution = [[row, col] for row, col in enumerate(solution)]
        print(formatted_solution)

solve(n)

