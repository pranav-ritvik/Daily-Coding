# cook your dish here
import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    best_even = 0 
    best_odd = 0  
    for v in a:
        if v % 2 == 0:
            best_even = max(best_even, best_odd + 1, 1)
        else:
            best_odd = max(best_odd, best_even + 1, 1)
    out.append(str(max(best_even, best_odd)))
print("\n".join(out))
