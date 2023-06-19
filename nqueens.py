def nqueens(n):
    col = set()
    posDiag = set()  # (r+c)
    negDiag = set()  # (r-c)
    result = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            board_instance = ["".join(row) for row in board]
            result.append(board_instance)
            return
        for c in range(n):
            if c in col or r + c in posDiag or r - c in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return result


ans = nqueens(4)
for i in ans:
    for j in i:
        print(j)
    print()
