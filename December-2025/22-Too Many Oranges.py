t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    if 10*N <= K <= 12*N:
        print("YES")
    else:
        print("NO")
