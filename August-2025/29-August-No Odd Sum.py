import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    c1 = a.count(1)
    c2 = n - c1
    if c1 == 0 or c2 == 0:
        out.append("0")
    elif c1 % 2 == 1:
        out.append(str(c2))
    else:
        out.append(str(min(c2, c1 // 2)))
print("\n".join(out))
