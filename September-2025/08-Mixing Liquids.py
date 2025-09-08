# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []

for _ in range(t):
    A = int(next(it)); B = int(next(it))
    x = min(A, B // 2)
    out.append(str(3 * x))

print("\n".join(out))
