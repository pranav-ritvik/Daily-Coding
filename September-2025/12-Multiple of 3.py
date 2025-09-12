# cook your dish here
N = int(input().strip())

low = (N // 3) * 3
high = low + 3

if abs(N - low) <= abs(N - high):
    print(low)
else:
    print(high)
