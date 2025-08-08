# cook your dish here
t = int(input())
for case in range(t):
    n, m = map(int, input().split())
    grid = []
    for r in range(n):
        grid.append(input().strip())
    count = 0
    for i in range(n):
        for j in range(m):
            max_len = min(n - i, m - j)
            for L in range(1, max_len):
                c = grid[i][j]
                if c == grid[i][j + L] == grid[i + L][j] == grid[i + L][j + L]:
                    count += 1
    print(count)
