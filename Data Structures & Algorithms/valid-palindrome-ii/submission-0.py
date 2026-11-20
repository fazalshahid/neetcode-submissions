class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isvalid(s):
            return s[:] == s[::-1]
        
        if isvalid(s):
            return True
        
        for i in range(len(s)):
            if isvalid(s[0:i] + s[i+1:]):
                return True
        
        return False