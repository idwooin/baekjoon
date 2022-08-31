row_visited = [0 for _ in range(9)]
column_visited = [0 for _ in range(9)]
square_visited = [0 for _ in range(9)]
sudoku = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    s = input()
    for j in range(9):
        a = int(s[j])
        sudoku[i][j] = a
        if a!=0:
            row_visited[i] |= (1<<a)
            column_visited[j] |= (1<<a)
            square_visited[3*(i//3)+(j//3)] |= (1<<a)

def dfs(curr):
    if curr == 81:
        return True
    row = curr//9
    col = curr%9

    if sudoku[row][col]!=0: return dfs(curr+1)

    for k in range(1,10):
        r = row_visited[row]&(1<<k)
        c = column_visited[col]&(1<<k)
        s = square_visited[3*(row//3)+(col//3)]&(1<<k)
        if not(r or c or s):
            sudoku[row][col] = k
            row_visited[row] |= (1<<k)
            column_visited[col] |= (1<<k)
            square_visited[3*(row//3)+(col//3)] |= (1<<k)
            if dfs(curr+1): return True
            sudoku[row][col] = 0
            row_visited[row] ^= (1<<k)
            column_visited[col] ^= (1<<k)
            square_visited[3*(row//3)+(col//3)] ^= (1<<k)
    
    return False

dfs(0)
for i in range(9):
    for j in range(9):
        sudoku[i][j] = str(sudoku[i][j])

for r in sudoku:
    print(''.join(r))