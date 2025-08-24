import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it)); c = int(next(it))
    friends = [int(next(it)) for _ in range(n)]
    s = set(friends)
    m = min(friends)

    if c not in s and m < c:
        out.append("0")
        continue

    y = c + 1 if c in s else c
    if y <= m:
        y = m + 1
    while y in s:
        y += 1
    out.append(str(y - c))

print("\n".join(out))
