t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    total = 0
    while A != B:
        if A > B:
            eat = (A + 1) // 2
            A -= eat
        else:
            eat = (B + 1) // 2
            B -= eat
        total += eat
    print(total)
