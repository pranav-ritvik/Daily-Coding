# cook your dish here
import sys
from collections import deque

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    s = next(it).strip()
    l, r = 0, n - 1
    T = deque()
    alice = True
    while l <= r:
        if alice:
            ch = s[l]; l += 1
            if ch == '0':
                T.appendleft('0')
            else:
                T.append('1')
        else:
            ch = s[r]; r -= 1
            if ch == '1':
                T.appendleft('1')
            else:
                T.append('0')
        alice = not alice
    out.append(''.join(T))
print('\n'.join(out))
