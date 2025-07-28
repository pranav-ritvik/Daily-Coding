# cook your dish here
t = int(input().strip())
for k in range(t):
    m, w = input().strip().split()
    i = 0
    j = 0
    while i < len(m) and j < len(w):
        if m[i] == w[j]:
            i += 1
        j += 1
    ok = i == len(m)

    i = 0
    j = 0
    while i < len(w) and j < len(m):
        if w[i] == m[j]:
            i += 1
        j += 1
    ok2 = i == len(w)

    if ok or ok2:
        print("YES")
    else:
        print("NO")
