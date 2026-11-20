class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []

        def backtrack(path, ind):
            #print(path)
            if sum(path) > target:
                return
            
            if sum(path) == target:
                self.result.append(path [:])
                return
            
            if ind == len(nums):
                return
            path.append(nums[ind])
            backtrack(path, ind)
            path.pop()

            for i in range(ind + 1, len(nums)):
                path.append(nums[i])
                backtrack(path, i)
                path.pop()
        path = []
        backtrack(path, 0)
        return self.result
            
