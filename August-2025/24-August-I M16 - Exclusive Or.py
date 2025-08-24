x = input().strip()
y = input().strip()

a = int(x, 2)
b = int(y, 2)

result = a ^ b

n = max(len(x), len(y))
print(format(result, f'0{n}b'))
