# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    odd = 0
    for _ in range(n):
        if int(next(it)) % 2 == 1:
            odd += 1
    out.append("Yes" if odd == 1 else "No")
print("\n".join(out))
