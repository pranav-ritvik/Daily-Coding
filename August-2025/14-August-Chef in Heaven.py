# cook your dish here
import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    L = int(next(it))
    S = list(next(it).strip())
    ones = 0
    ok = False
    for i, ch in enumerate(S, 1):
        if ch == '1':
            ones += 1
        if ones * 2 >= i:
            ok = True
            break
    out.append("YES" if ok else "NO")
print("\n".join(out))
