import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        q = []
        for point in points:
            dis = math.sqrt(point[0]**2 + point[1]**2)

            if not q or len(q) < k:
                heapq.heappush(q, (-dis, point))
            
            elif -dis > q[0][0]:
                heapq.heappop(q)
                heapq.heappush(q, (-dis, point))
        
        return [p[1] for p in q]
        