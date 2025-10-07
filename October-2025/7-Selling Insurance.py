import math
t = int(input())
for _ in range(t):
    x = int(input())
    commission = 0.2 * x
    ans = math.ceil(100 / commission)
    print(ans)
