class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def getPivot(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return i + 1
            return 0
        
        return nums[getPivot(nums)]