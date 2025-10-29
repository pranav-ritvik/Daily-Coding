class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if s == s[::-1]:
        #     return True
        # left = 0
        # flag = False
        # right = len(s)-1
        # while left < right:
        #     if s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         if not flag:
        #             l1 , r1 = left+1 , right
        #             l2 , r2 = left, right-1
        #             if s[l1] == s[r1]:
        #                 flag = False
        #                 left = l1
        #                 right = r1
        #             elif s[l2] == s[r2]:
        #                 flag = False
        #                 left = l2
        #                 right = r2
        #         else:
        #             return False
        # return True
        def is_palindrome(sub):
            return sub == sub[::-1]  
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        
        return True



