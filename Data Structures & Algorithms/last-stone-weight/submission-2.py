class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            x = stones[-1]
            y = stones [-2]

            if x == y:
                stones.pop()
                stones.pop()

            elif x > y:
                stones.pop()
                stones[-1] = x - y
            else:
                stones.pop()
                stones[-1] = y - x
            stones.sort()
        return stones[-1] if stones else 0

