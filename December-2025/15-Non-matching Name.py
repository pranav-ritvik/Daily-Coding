t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    SA = input().strip()
    SB = input().strip()
    
    used = set(SA) | set(SB)
    
    if len(used) < 26:
        print("YES")
    else:
        print("NO")
