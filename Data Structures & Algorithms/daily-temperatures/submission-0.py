class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        stack = [0]

        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return result
        