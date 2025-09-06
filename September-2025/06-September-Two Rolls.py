# cook your dish here
import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    x = int(next(it)); y = int(next(it))
    s = 50 - x
    out.append("Yes" if 2*y <= s <= 2*y + 10 else "No")
print("\n".join(out))
