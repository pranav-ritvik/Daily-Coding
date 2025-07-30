# cook your dish here
from collections import Counter

n = int(input().strip())
strings = [input().strip() for _ in range(n)]

min_freq = [float('inf')] * 26
for s in strings:
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    for i in range(26):
        min_freq[i] = min(min_freq[i], freq[i])

result = ""
for i in range(26):
    if min_freq[i] != float('inf'):
        result += chr(i + ord('a')) * min_freq[i]

print(result if result else "no such string")
