class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in cache:
                return [cache[comp], i]
            
            cache[num] = i

        