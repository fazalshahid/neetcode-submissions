class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            n = len(s)
            res += f"{n}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #print(s)
        while i < len(s):
            #print(s[i])
            n = ''
            while s[i].isdigit():
                n += s[i]
                i += 1
            #print(n)
            n = int(n)

            curStr = ''
            for j in range(i + 1, i + n + 1):
                curStr += s[j]
            res.append(curStr)
            i = i + n + 1
        
        return res



