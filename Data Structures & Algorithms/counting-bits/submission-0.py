class Solution:
    def numBits(self, n):
        res = 0

        for i in range(32):
            if 1 << i & n:
                res += 1
        return res
    def countBits(self, n: int) -> List[int]:

        res = []
        for i in range(0, n + 1):
            res.append(self.numBits(i))
        return res

        