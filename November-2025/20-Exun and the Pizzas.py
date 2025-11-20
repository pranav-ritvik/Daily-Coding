# cook your dish here
N, K, R = map(int, input().split())
remaining = N - K
revenue = remaining * R
print(revenue)
