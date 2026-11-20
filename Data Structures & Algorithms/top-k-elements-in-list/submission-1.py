from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        q = []
        for num, count in freq.items():
            if len(q) < k:
                heapq.heappush(q, (count, num))
            elif count > q[0][0]:
                heapq.heappop(q)
                heapq.heappush(q, (count, num))
        return [f [1] for f in q]


        