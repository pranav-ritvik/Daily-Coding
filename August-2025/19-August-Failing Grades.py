# cook your dish here
import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
res = []
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    ok = True
    s = 0
    for i, v in enumerate(a, 1):
        s += v
        if s < 40 * i:
            ok = False
            break
    res.append("Yes" if ok else "No")
print("\n".join(res))
