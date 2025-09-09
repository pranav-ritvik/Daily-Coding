# cook your dish here
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it))
    s = next(it).strip()

    ok = True
    i = 0
    while i < n:
        if s[i] == '1':
            j = i
            while j < n and s[j] == '1':
                j += 1
            run_len = j - i
            if run_len in (1, 2):
                ok = False
                break
            i = j
        else:
            i += 1

    out.append("Yes" if ok else "No")

print("\n".join(out))
