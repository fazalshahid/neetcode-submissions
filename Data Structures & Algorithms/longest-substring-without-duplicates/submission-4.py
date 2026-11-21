class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = {}
        left = 0

        for right, ch in enumerate(s):
            #print(seen)
            if ch in seen:
                left = max(left, seen[ch] + 1)
            longest = max (right - left + 1, longest)
            seen[ch] = right
        return longest
