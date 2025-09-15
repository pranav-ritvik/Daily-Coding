# cook your dish here

t = int(input())  
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    min_val = min(arr)
    max_val = max(arr)
    
    ans = max(0, max_val - min_val - 1)
    print(ans)
