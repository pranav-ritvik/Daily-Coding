# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    boys, girls = 0, 0
    entered = 0
    closed = False
    
    for ch in s:
        if ch == 'B':
            boys += 1
        else:
            girls += 1
        entered += 1
        
        if boys > 2 * girls:
            closed = True
            break
    
    print(entered if closed else n)
