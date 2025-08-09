# cook your dish here
t = int(input())
for case in range(t):
    n, b = map(int, input().split())
    best_area = 0
    for i in range(n):
        w, h, p = map(int, input().split())
        if p <= b:
            area = w * h
            if area > best_area:
                best_area = area
    print(best_area if best_area > 0 else "no tablet")
