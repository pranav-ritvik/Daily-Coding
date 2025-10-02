# cook your dish here
t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort(reverse=True)       
    print(sum(prices[:k]))         
