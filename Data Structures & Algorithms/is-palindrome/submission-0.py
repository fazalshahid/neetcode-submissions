class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = ''

        for ch in s:
            if ch.isalnum():
                parsed += ch.lower()
        
        s = parsed
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        