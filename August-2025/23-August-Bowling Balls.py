# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it)); x = int(next(it)); y = int(next(it))
    cnt = 0
    for _ in range(n):
        v = int(next(it))
        if x <= v <= y:
            cnt += 1
    out.append(str(cnt))
print("\n".join(out))
