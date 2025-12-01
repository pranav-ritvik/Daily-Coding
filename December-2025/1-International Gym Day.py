# cook your dish here
t = int(input())
for _ in range(t):
    D, X, Y = map(int, input().split())
    ans = -1

    # Try all possible numbers of trial sessions n
    for n in range(Y + 1):  # can't do more sessions than coins
        discount = n * D

        # If discount is 100% or more, membership is free or <= 0
        if discount >= 100:
            # Just need to afford the n sessions
            if n <= Y:
                ans = n
                break
            else:
                break

        # Coins left after paying for n sessions
        left = Y - n

        # Check: left * 100 >= X * (100 - discount)
        if left * 100 >= X * (100 - discount):
            ans = n
            break

    print(ans)
