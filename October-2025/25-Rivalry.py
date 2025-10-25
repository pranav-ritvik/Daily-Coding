r1, r2 = map(int, input().split())
d1, d2 = map(int, input().split())

final1 = r1 + d1
final2 = r2 + d2

if final1 > final2:
    print("Dominater")
else:
    print("Everule")
