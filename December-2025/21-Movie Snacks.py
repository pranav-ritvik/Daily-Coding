X, Y, Z = map(int, input().split())

ans = float('inf')
for c in range(3):  # c = 0,1,2 combos
    if c <= 2 and c <= 3:
        cost = c * Z + (2 - c) * X + (3 - c) * Y
        ans = min(ans, cost)

print(ans)
