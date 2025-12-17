T = int(input())
for _ in range(T):
    N = int(input())
    f = g = 0

    for d in range(1, N+1):
        if N % d == 0:
            if d % 2 == 0:
                f += 1
            else:
                g += 1

    if f > g:
        print(1)
    elif f == g:
        print(0)
    else:
        print(-1)
