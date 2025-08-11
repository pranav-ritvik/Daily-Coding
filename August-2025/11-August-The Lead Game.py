# cook your dish here
n = int(input())
cum1 = 0
cum2 = 0
best_lead = 0
winner = 0
for i in range(n):
    s, t = map(int, input().split())
    cum1 += s
    cum2 += t
    if cum1 >= cum2:
        lead = cum1 - cum2
        if lead > best_lead:
            best_lead = lead
            winner = 1
    else:
        lead = cum2 - cum1
        if lead > best_lead:
            best_lead = lead
            winner = 2
print(winner, best_lead)
