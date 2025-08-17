# cook your dish here
import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    B = [int(next(it)) for _ in range(n)]

    bucket = [0]*101  # B_i in [1..100]
    for a, b in zip(A, B):
        if a > 0 and 1 <= b <= 100:
            bucket[b] += a

    best = 0  
    cur = 0
    for L in range(1, 101):
        cur += bucket[L]
        best = max(best, cur - L)

    out.append(str(best))

print("\n".join(out))
