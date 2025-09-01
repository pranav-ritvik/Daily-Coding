# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
    x = int(next(it))
    out.append("3" if x % 3 == 0 else "1")
print("\n".join(out))
