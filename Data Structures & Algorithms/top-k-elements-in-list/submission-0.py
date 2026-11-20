from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        ans = []

        for num, freq in counter.items():
            if (len(ans) < k):
                heapq.heappush(ans, (freq, num))
                continue
            
            if freq > ans[0][0]:
                heapq.heappop(ans)
                heapq.heappush(ans, (freq, num))
        
        return [v[1] for v in ans]
        
        