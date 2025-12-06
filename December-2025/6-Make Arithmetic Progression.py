# cook your dish here
t = int(input())
for _ in range(t):
    X, Y, Z = map(int, input().split())
    
    if 2 * Y == X + Z:
        print(0)
    else:
        print(1)
