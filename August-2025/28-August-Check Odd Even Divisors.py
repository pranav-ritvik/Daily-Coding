# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
    A = int(next(it)); B = int(next(it))
    out.append("Yes" if A >= 1 and B % A == 0 else "No")
print("\n".join(out))
