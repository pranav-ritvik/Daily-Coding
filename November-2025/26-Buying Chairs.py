t = int(input())
for _ in range(t):
    W, P, K = map(int, input().split())
    
    wood_used = min(W, K)
    plastic_used = K - wood_used
    
    print(wood_used * 2 + plastic_used)
