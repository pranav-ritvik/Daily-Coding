# cook your dish here
import sys
import math

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
    x = int(next(it)); y = int(next(it))
    if math.gcd(x, y) > 1:
        out.append("0")
    elif math.gcd(x + 1, y) > 1 or math.gcd(x, y + 1) > 1:
        out.append("1")
    else:
        out.append("2")
print("\n".join(out))
