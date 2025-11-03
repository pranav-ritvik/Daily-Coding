t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    diff = b + 10 - a
    if diff <= 0:
        print(0)
    else:
        print((diff + 2) // 3)
