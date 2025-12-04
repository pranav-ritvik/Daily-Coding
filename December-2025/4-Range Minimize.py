t = int(input())
for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    # Calculate the 3 possible ranges
    r1 = A[-1] - A[2]     # remove A[0], A[1]
    r2 = A[-2] - A[1]     # remove A[0], A[-1]
    r3 = A[-3] - A[0]     # remove A[-1], A[-2]

    print(min(r1, r2, r3))
