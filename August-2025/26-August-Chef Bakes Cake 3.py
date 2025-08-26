# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    mx = max(a)
    best = 0
    for x in range(mx + 1):
        sold = sum(min(x, v) for v in a)
        profit = 50 * sold - 30 * x * n
        if profit > best:
            best = profit
    out.append(str(best))

print("\n".join(out))
