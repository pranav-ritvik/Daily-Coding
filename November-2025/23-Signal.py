t = int(input())
for _ in range(t):
    N = int(input())
    S = input().strip()
    
    seen_zero = False
    count = 0
    
    for ch in S:
        if ch == '0':
            seen_zero = True
        elif seen_zero and ch == '1':
            count += 1
    
    print(count)
