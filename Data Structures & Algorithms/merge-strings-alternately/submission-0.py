class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i1 = 0
        i2 = 0

        res = ''
        while i1 < len(word1) or i2 < len(word2):
            merged = ''

            if i1 < len(word1):
                merged += word1[i1]
                i1 += 1
            
            if i2 < len(word2):
                merged += word2[i2]
                i2 += 1
            
            res += merged
        return res

