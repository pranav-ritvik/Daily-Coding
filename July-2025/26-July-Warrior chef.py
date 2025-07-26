# cook your dish here
def canWin(arr, health, resistance):
    for enemy in arr:
        if enemy > resistance:
            if health <= enemy:
                return False
            health -= enemy
    return health > 0

testCases = int(input())
for t in range(testCases):
    n, h = map(int, input().split())
    enemies = list(map(int, input().split()))
    low = 0
    high = max(enemies)
    answer = high
    while low <= high:
        mid = (low + high) // 2
        if canWin(enemies, h, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    print(answer)
