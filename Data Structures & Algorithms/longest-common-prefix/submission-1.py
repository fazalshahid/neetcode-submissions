class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ''

        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if len(s) -1 < i or s[i] != ch:
                    return longest
            longest += ch
        return longest
                
                