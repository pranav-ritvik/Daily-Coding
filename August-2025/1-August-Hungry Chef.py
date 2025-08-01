# cook your dish here
t = int(input())
for test_case in range(t):
    X, Y, N, R = map(int, input().split())
    min_cost = N * X
    max_cost = N * Y
    if R < min_cost:
        print(-1)
    elif R >= max_cost:
        print(0, N)
    else:
        max_premium = (R - N * X) // (Y - X)
        if max_premium > N:
            max_premium = N
        print(N - max_premium, max_premium)
