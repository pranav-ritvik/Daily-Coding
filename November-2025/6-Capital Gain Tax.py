x, y = map(int, input().split())

if y > x:
    print("INCREASED")
elif y < x:
    print("DECREASED")
else:
    print("SAME")
