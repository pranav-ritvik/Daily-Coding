# cook your dish here
import sys

lines = sys.stdin.read().splitlines()
t = int(lines[0])
out = []
for idx in range(1, t + 1):
    s = lines[idx].strip()
    bal = 0
    best = 0
    for i, ch in enumerate(s, 1):
        bal += 1 if ch == '<' else -1
        if bal < 0:
            break
        if bal == 0:
            best = i
    out.append(str(best))
print("\n".join(out))
