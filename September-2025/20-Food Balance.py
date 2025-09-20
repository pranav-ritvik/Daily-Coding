# cook your dish here
f1, p1, f2, p2 = map(int, input().split())

d1 = abs(f1 - p1)
d2 = abs(f2 - p2)

if d1 < d2:
    print("First")
elif d2 < d1:
    print("Second")
else:
    print("Both")
