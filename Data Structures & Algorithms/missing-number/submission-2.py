class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxx = len(nums)

        expected = maxx * (maxx + 1) // 2

        summ = sum(nums)

        return expected - summ