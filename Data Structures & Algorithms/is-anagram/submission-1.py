from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = defaultdict(int)
        t_counter = defaultdict(int)

        def build(strr, counter):
            for ch in strr:
                counter[ch] += 1
        
        build(s, s_counter)
        build(t, t_counter)

        return s_counter == t_counter

