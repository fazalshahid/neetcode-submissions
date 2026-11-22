class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            result = None
            try:
                num = int(token)
            except Exception as e:

                if token == '+':
                    result = stack[-2] + stack[-1]
                if token == '-':
                    result = stack[-2] - stack[-1]
                if token == '*':
                    result = stack[-2] * stack[-1]
                if token == '/':
                    result = int(stack[-2] / stack[-1])
                print(result)
                stack.pop()
                stack.pop()
            
            num = result if result is not None else num
            stack.append(num)
        return stack[-1]