class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = math.inf
        ci = -1
        for i, num in enumerate(arr):
            if abs(num - x) < closest:
                closest = abs(num - x)
                ci = i
        
    
        res = [arr[ci]]
        left = 1
        right = 1
        while len(res) < k:
            if ci - left >= 0 and ci + right < len(arr):
                if abs(arr[ci-left] - x) <= abs(arr[ci + right] - x):
                    res.append(arr[ci-left])
                    left += 1
                else:
                    res.append(arr[ci + right])
                    right += 1
            elif ci - left > 0:
                res.append(arr[ci-left])
                left += 1
            else:
                res.append(arr[ci + right])
                right += 1
        
        return sorted(res)



