t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    total_time = x * y
    available_time = z * 24 * 60
    if total_time <= available_time:
        print("YES")
    else:
        print("NO")
