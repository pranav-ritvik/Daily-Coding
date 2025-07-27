# cook your dish here
t = int(input())
for test in range(t):
    n = int(input())
    odd = 1
    even = 2
    mat = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                mat[i][j] = odd
                odd += 2
            else:
                mat[i][j] = even
                even += 2

    for row in mat:
        print(*row)
