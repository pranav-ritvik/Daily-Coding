# CodeChef: Max Triangle

t = int(input())   # number of test cases
for _ in range(t):
    n = int(input())
    if n > 3:
        print(3 * n - 3)   # perimeter of (n, n-1, n-2)
    else:
        print(-1)          # not possible
