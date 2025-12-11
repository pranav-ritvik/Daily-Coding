t = int(input())
for _ in range(t):
    N = int(input())
    S = N // 2   # L + B must be <= S

    if S < 2:
        print(0)
        continue

    L = S // 2
    B = S - L
    print(L * B)
