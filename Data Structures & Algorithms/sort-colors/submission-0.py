from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)

        last = 0
        for i in range(3):
            for j in range(counter[i]):
                nums[last+j] = i
            last += counter[i]
        