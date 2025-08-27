# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    odd = sum(1 for d in range(1, n + 1) if n % d == 0 and d % 2 == 1)
    even = sum(1 for d in range(1, n + 1) if n % d == 0 and d % 2 == 0)
    out.append(f"{odd} {even}")
print("\n".join(out))
