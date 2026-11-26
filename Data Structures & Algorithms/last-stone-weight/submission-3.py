class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        while len(stones) > 1:
            stones.sort()
            h1 = stones.pop()
            h2 = stones.pop()
            if h1 == h2:
                continue
            stones.append(h1 - h2)
        
        return 0 if not stones else stones[0]

