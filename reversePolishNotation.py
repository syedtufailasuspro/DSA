class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+*/-":
                opr2 = int(stack.pop())
                opr1 = int(stack.pop())
                if i == "+":
                    res = opr1 + opr2
                    stack.append(res)
                elif i == "-":
                    res = opr1 - opr2
                    stack.append(res)
                elif i == "*":
                    res = opr1 * opr2
                    stack.append(res)
                else:
                    res = opr1 / opr2
                    stack.append(res)
                
            else:
                stack.append(i)
                

        return int(stack.pop())


        