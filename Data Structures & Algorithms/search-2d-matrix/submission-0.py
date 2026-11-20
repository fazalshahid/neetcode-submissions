class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        lr, hr = 0, m-1

        while lr <= hr:
            mr = lr + (hr - lr) // 2

            if target < matrix[mr][0]:
                hr = mr - 1
                continue
            if target > matrix[mr][n-1]:
                lr = mr + 1
                continue

            lc, hc = 0, n - 1


            while lc <= hc:
                mc = lc + (hc - lc) // 2

                if matrix[mr][mc] == target:
                    return True
                
                if matrix[mr][mc] < target:
                    lc = mc + 1
                else:
                    hc = mc - 1
            return False
        return False
            