# cook your dish here
import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
ans = []
for _ in range(t):
    n = int(next(it))
    m = int(next(it))
    have = {int(next(it)) for _ in range(n)}
    ans.append(str(m - len(have)))
print("\n".join(ans))
