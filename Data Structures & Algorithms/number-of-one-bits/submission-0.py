class Solution:
    def hammingWeight(self, n: int) -> int:
        def binary(num):
            res = []

            while num:
                res.append(num % 2)
                num //= 2
            
            return res[::-1]
        
        bits = binary(n)

        count = 0
        for bit in bits:
            if bit:
                count += 1
        return count