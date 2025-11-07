T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    total = X * Y
    if total <= Z:
        print(0)
    else:
        max_sources = Z // Y
        print(X - max_sources)
