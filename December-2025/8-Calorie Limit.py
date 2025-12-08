t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    sum_cal = 0
    count = 0
    
    for x in A:
        if sum_cal + x <= K:
            sum_cal += x
            count += 1
        else:
            break
    
    print(count)
