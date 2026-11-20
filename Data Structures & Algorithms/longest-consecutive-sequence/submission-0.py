class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 0
        for num in nums:
            count = 1

            if num - 1 in nums_set:
                continue
            while num + 1 in nums_set:
                count += 1
                num += 1
            res = max(res, count)
        return res

