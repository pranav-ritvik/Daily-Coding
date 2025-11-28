t = int(input())
for _ in range(t):
    N, X = map(int, input().split())
    
    if N <= X:
        print(0)
    else:
        M = N - X
        profit = M * (M + 1) // 2
        print(profit)
