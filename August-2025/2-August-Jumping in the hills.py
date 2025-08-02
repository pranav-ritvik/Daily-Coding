# cook your dish here
T = int(input())
for case in range(T):
    N, U, D = map(int, input().split())
    heights = list(map(int, input().split()))
    parachute = 1
    position = 1
    for i in range(N - 1):
        if heights[i + 1] == heights[i]:
            position += 1
        elif heights[i + 1] > heights[i]:
            if heights[i + 1] - heights[i] <= U:
                position += 1
            else:
                break
        else: 
            if heights[i] - heights[i + 1] <= D:
                position += 1
            elif parachute:
                parachute = 0
                position += 1
            else:
                break
    print(position)
