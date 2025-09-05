# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
ans = []
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    odd_days_sum = sum(a[0::2])
    even_days_sum = sum(a[1::2])
    ans.append(str(max(odd_days_sum, even_days_sum)))
print("\n".join(ans))
