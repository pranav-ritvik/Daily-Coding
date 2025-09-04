# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it)); c = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    B = [int(next(it)) for _ in range(n)]

    # cheapest cost per vitamin type
    INF = 10**9
    min_cost = [INF] * (n + 1)  # vitamins are in [1..N]
    for a, b in zip(A, B):
        if b < min_cost[a]:
            min_cost[a] = b

    ans = 0
    for cost in min_cost:
        if cost != INF:
            gain = c - cost
            if gain > 0:
                ans += gain

    out.append(str(ans))

print("\n".join(out))
