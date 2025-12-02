X, Y, Z = map(int, input().split())

played = X + Y + Z
rem = 4 - played   # remaining games

if X + rem > Z:
    print("YES")
else:
    print("NO")
