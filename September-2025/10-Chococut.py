# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []

for _ in range(t):
    N = int(next(it)); M = int(next(it)); K = int(next(it))
    total = N * M
    best = 0

    if K == 0:
        best = total
    else:
        # Horizontal cuts
        for r in range(1, N):
            part = r * M
            other = total - part
            if part >= K:
                best = max(best, other)
            if other >= K:
                best = max(best, part)
        # Vertical cuts
        for c in range(1, M):
            part = c * N
            other = total - part
            if part >= K:
                best = max(best, other)
            if other >= K:
                best = max(best, part)

        # Giving entire bar to Bob
        if total >= K:
            best = max(best, 0)

    out.append(str(best))

print("\n".join(out))
