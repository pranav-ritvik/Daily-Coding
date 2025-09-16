# cook your dish here

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # max breaks = sum of (Ai - 1)
    ans = sum(arr) - n
    print(ans)
