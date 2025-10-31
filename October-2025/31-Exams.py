# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    total = x * y
    if z > total / 2:
        print("YES")
    else:
        print("NO")
