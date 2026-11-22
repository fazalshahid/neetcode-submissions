class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_pivot():
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                print(f"{left} {mid} {right}")
                if mid == left or mid == right:
                    return mid

                if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                    print("bbbbbb")
                    return mid
                
                if nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid
        
        def binary_search(left, right):

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    #print("bbbb")
                    return mid
                if target > nums[mid]:
                    left += 1
                else:
                    right -= 1
            return -1
        pivot = get_pivot()
        print(nums[pivot])
        res = binary_search(0, pivot)
        if res > -1:
            return res
        return binary_search(pivot + 1, len(nums) - 1)
        
        
        
