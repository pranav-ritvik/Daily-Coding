t = int(input())
for _ in range(t):
    N, X = map(int, input().split())
    odd = (N + 1) // 2
    even = N // 2

    if X % 2 == 0:   # X is even
        print(even - 1)
    else:            # X is odd
        print(odd - 1)
