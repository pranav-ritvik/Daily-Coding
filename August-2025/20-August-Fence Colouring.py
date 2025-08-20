# cook your dish here
import sys
from collections import Counter

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    freq = Counter(A)
    cnt_not1 = n - freq.get(1, 0)
    maxfreq = max(freq.values())
    ans = min(cnt_not1, 1 + (n - maxfreq))  
    out.append(str(ans))
print("\n".join(out))
