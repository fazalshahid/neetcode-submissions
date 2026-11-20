from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)

        lucky = -1
        for num in arr:
            if counter[num] == num and num > lucky:
                lucky = num
        return lucky 