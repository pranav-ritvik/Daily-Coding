class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div = []
        no = []
        for i in range(1,n+1):
            if i%m == 0:
                div.append(i)
            else:
                no.append(i)
        return sum(no)-sum(div)
