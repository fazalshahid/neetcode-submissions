import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        minn = high
        while low <= high:
            mid = (low + high) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / mid)

            if time <= h:
                minn = min(minn, mid)
                high = mid - 1
            else:
                low = mid + 1
        return minn
                