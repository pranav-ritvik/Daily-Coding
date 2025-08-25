class Solution:
    def maxSubArray(self, nums):
        best = nums[0]
        cur = nums[0]

        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            best = max(best, cur)

        return best
