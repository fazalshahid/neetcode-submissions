class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twoSum(target, ind):
            left = 0
            right = len(nums)-1
            res = []
            while left < right:
                if left == ind:
                    left += 1
                    continue
                if right == ind:
                    right -= 1
                    continue

                summ = nums[left] + nums[right]
                if summ == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                if summ > target:
                    right -= 1
                else:
                    left += 1
            return res
        ans = set()
        for i in range(len(nums)):
            results = twoSum(-nums[i], i)
            if not results:
                continue
            #res = ",".join(sorted(res))
            #print(res)
            #print(ans)
            #print(",".join([sorted(res + [nums[i]])))
            for res in results:
                ans.add(",".join([str(x) for x in sorted(res + [nums[i]])]))
        
        ans_list = []

        for triplet in ans:
            l = triplet.split(",")

            ans_list.append([int(v) for v in l])
        return ans_list
        