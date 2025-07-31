# cook your dish here
t = int(input().strip())
for _ in range(t):
    word = input().strip()
    total = 1 + 1  # LOAD + PRINT
    for i in range(1, len(word)):
        steps = (ord(word[i]) - ord(word[i-1]) + 26) % 26
        total += steps + 1
    print("YES" if total <= 11 * len(word) else "NO")
