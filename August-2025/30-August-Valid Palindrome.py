class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = ''
        for char in s:
            if char.isalnum():
                s2 = s2 + char
        s2 = list(s2)

        print(s2)
        print(s2[::-1])
        if s2 == s2[::-1]:
            return True
        else:
            return False
