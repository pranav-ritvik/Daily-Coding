# cook your dish here
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    requests = list(map(int, input().split()))
    result = ""
    for amount in requests:
        if amount <= K:
            result += "1"
            K -= amount
        else:
            result += "0"
    print(result)
