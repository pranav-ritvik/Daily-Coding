# cook your dish here
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    mx = max(a, b, c)
    total = a + b + c - mx
    if mx - total <= 1:
        print("YES")
    else:
        print("NO")
