# cook your dish here
def max_dollars(n, memo):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    
    memo[n] = max(n, max_dollars(n//2, memo) + max_dollars(n//3, memo) + max_dollars(n//4, memo))
    return memo[n]

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

memo = {}
for n in nums:
    print(max_dollars(n, memo))
