# cook your dish here
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, x = map(int, sys.stdin.readline().split())
    ans = (1 << (n + 1)) - (1 << (n - x + 2)) + 2
    print(ans)
