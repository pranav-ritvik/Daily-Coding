t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    min_distance = 1000000
    for i in range(n):
        x, y = map(int, input().split())
        distance = abs(x - a) + abs(y - b)
        if distance < min_distance:
            min_distance = distance
    print(min_distance)
