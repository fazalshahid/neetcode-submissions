class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sum_dig(n: int) -> int:
            digits = str(n)

            res = 0

            for ch in digits:
                digit = int(ch)

                res += digit ** 2
            return res
        
        result = True
        while result:
            n = sum_dig(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
        