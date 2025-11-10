# cook your dish here
T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))

    switches = 0
    current_gun = 0  # start with close-range gun

    for dist in A:
        required_gun = 0 if dist <= D else 1
        if required_gun != current_gun:
            switches += 1
            current_gun = required_gun

    print(switches)
