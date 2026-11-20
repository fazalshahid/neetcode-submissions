class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        high = sum(weights)
        low = max(weights)

        print(low)
        print(high)
        res = None
        while low <= high:
            mid = low + (high - low) // 2

            count = 1
            avail = mid
            print("=======")
            print(mid)
            print("========")
            for w in weights:
                if w > avail:
                    count += 1
                    avail = mid
                avail -= w
            
            if count <= days:
                res = mid
            
            if count > days:
                low = mid + 1
            else:
                high = mid - 1
        
        return res




