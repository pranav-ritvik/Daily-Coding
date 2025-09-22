# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    chef_score = a[0]
    
    # Find cutoff: max of scores strictly less than chef_score
    cutoff = 0
    for score in a:
        if score < chef_score and score + 1 > cutoff:
            cutoff = score + 1
    
    # Ensure cutoff ≤ chef_score
    if cutoff > chef_score:
        cutoff = chef_score
    
    # Count students with score ≥ cutoff
    passed = sum(1 for score in a if score >= cutoff)
    print(passed)
