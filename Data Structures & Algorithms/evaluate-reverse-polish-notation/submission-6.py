class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '*', '-', '/']
        

        stack = []

        for token in tokens:
            print(stack)
            if len(stack) > 1 and token in operands:
                top1 = stack.pop()
                top2 = stack.pop()
                if token == '+':
                    stack.append(top1 + top2)
                if token == "-":
                    stack.append(top2 - top1)
                if token == '*':
                    stack.append(top1 * top2)
                if token == '/':
                    stack.append(int(top2/top1))

            if token not in operands:
                stack.append(int(token))

        return stack[-1]
                    



        