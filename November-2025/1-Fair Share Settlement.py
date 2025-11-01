# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    fair_share = n / (k + 1)        
    paid_back = k * int(fair_share) 
    print(n - paid_back)
