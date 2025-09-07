# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
ans = []

for _ in range(t):
    n = int(next(it))
    best = 10**9
    for three in range(n // 3 + 1):  # try 0..floor(n/3) three-flower packs
        rem = n - 3 * three
        if rem % 2 == 0:
            two = rem // 2
            cost = three * 5 + two * 4
            best = min(best, cost)
    ans.append(str(best))

print("\n".join(ans))
