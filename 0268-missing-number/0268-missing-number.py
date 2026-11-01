class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        sum1 = 0

        for i in nums:
            
            sum1 = sum1 + i

        return total - sum1


        