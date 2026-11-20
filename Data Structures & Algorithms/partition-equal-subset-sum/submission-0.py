class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)

        def backtrack(curSum, target, ind):
            if curSum == target:
                return True
            
            if ind == len(nums):
                return False
            
            for i in range(ind, len(nums)):
                curSum += nums[i]
                if backtrack(curSum, summ - curSum, i + 1):
                    return True
                curSum -= nums[i]
            return False
        return backtrack(0, summ, 0)
