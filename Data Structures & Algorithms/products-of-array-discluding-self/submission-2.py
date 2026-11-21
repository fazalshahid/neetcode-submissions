class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        res = [1]
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            res.append(prod)
        prod = 1
        for i in range(len(nums)-2, -1, -1):
            prod *= nums[i+1]
            res [i] *= prod
        #print(res)
        return res
            

        