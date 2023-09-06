from collections import defaultdict
def validSudoku(board):
    check_rows = defaultdict(set)
    check_cols = defaultdict(set)
    check_squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            currentNum = board[r][c]
            if board[r][c] == '.':
                continue
            if board[r][c] in check_rows[r]:
                return False
            if board[r][c] in check_cols[c]:
                return False
            if board[r][c] in check_squares[(r//3, c//3)]:
                return False
            check_rows[r].add(board[r][c])
            check_cols[c].add(board[r][c])
            check_squares[(r//3, c//3)].add(board[r][c])
    
    print(check_squares)

    return True

def main():
    board1 = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    print(validSudoku(board1))

if __name__ == "__main__":
    main()