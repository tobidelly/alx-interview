#!/usr/bin/python3
import sys

def print_solution(solution):
    # Print each solution in the required format: list of [row, col] positions.
    print([[row, col] for row, col in enumerate(solution)])

def is_safe(solution, row, col):
    # Check if placing a queen at (row, col) is safe
    for i in range(row):
        if solution[i] == col or \
           solution[i] - i == col - row or \
           solution[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row=0, solution=[]):
    # Recursive backtracking function to find all solutions
    if row == n:
        print_solution(solution)
        return
    for col in range(n):
        if is_safe(solution, row, col):
            solution.append(col)
            solve_nqueens(n, row + 1, solution)
            solution.pop()

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate if N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve the N-Queens puzzle
    solve_nqueens(n)

if __name__ == "__main__":
    main()

