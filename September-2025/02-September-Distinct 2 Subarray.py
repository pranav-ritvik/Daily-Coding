# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]

    ans = -1
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            ans = 2
            break

    if ans == -1:
        if len(set(a)) >= 2:
            ans = 3
        else:
            ans = -1

    out.append(str(ans))

print("\n".join(out))
