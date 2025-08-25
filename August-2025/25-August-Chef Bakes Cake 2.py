# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    cost = 0
    for i in range(N):
        if A[i] > B[i]:
            cost += A[i] - B[i]
    
    print(cost)
