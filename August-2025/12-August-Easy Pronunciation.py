# cook your dish here
t = int(input())
vowels = {'a', 'e', 'i', 'o', 'u'}

for _ in range(t):
    n = int(input())
    s = input().strip()

    count = 0
    hard = False

    for ch in s:
        if ch not in vowels:
            count += 1
            if count >= 4:
                hard = True
                break
        else:
            count = 0

    print("NO" if hard else "YES")
