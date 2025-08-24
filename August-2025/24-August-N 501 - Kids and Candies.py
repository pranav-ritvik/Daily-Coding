# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
A = set(map(int, input().split()))
m = int(input().strip())
C = list(map(int, input().split()))
for num in C:
    if num in A:
        print("Happy Halloween!")
    else:
        print("Tricky!")
