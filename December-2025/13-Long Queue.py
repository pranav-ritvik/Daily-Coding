t = int(input())
for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    
    X = A[-1]  # Sushil's wealth
    i = N - 2  # person directly in front
    
    while i >= 0 and A[i] * 2 <= X:
        i -= 1   # bully and remove
    
    # final position = index + 2
    print(i + 2)
