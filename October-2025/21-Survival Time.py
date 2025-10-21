t = int(input())
for _ in range(t):
    n, x, d = map(int, input().split())
    daily_need = 5 * x
    if n < daily_need:
        print(d)
    else:
        full_days = n // daily_need
        print(full_days + d)
