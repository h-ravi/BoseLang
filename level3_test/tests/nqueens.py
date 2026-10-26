import time

def is_safe(board, row, col):
    for r in range(1, row):
        c = board[r]
        if c == col:
            return False
        diff_c = c - col
        if diff_c < 0:
            diff_c = -diff_c
        diff_r = row - r
        if diff_r < 0:
            diff_r = -diff_r
        if diff_c == diff_r:
            return False
    return True

def solve(board, row, n):
    if row > n:
        return 1
    count = 0
    for col in range(1, n + 1):
        if is_safe(board, row, col):
            board[row] = col
            count += solve(board, row + 1, n)
    return count

n = 10
board = [0] * (n + 1)

start = time.perf_counter()
total = solve(board, 1, n)
end = time.perf_counter()

print("RESULT:", total)
print("TIME:", (end - start) * 1000.0)
