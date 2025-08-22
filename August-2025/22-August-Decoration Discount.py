# cook your dish here
import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
ans = []

for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    best_adj = float('inf')
    for i in range(n - 1):
        best_adj = min(best_adj, a[i] + a[i + 1] // 2)
    best_nonadj = float('inf')
    pref_min = a[0]
    for j in range(2, n):
        pref_min = min(pref_min, a[j - 2])
        best_nonadj = min(best_nonadj, pref_min + a[j])
    ans.append(str(min(best_adj, best_nonadj)))

print("\n".join(ans))
