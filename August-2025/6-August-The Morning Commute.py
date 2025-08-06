# cook your dish here
test_cases = int(input())
for case_number in range(test_cases):
    n = int(input())
    time = 0
    for line_number in range(n):
        xi, li, fi = map(int, input().split())
        if time < xi:
            time = xi
        else:
            wait = (fi - (time - xi) % fi) % fi
            time += wait
        time += li
    print(time)
