t = int(input())
for _ in range(t):
    N = int(input())
    max_speed = -1
    winner = 1
    
    for i in range(1, N+1):
        d, ti = map(int, input().split())
        speed = d // ti
        
        if speed > max_speed:
            max_speed = speed
            winner = i
    
    print(winner)
