class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = list(s)
        print(stack)
        def solve(stack):
            res = ''
            while stack:
                num = ''
                val = stack.pop()
                if val.isalpha():
                    res = val + res
                elif val == ']':
                    val = solve(stack)
                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    res = int(num) * val + res
                
                elif val == '[':
                    break
            return res
        
        return solve(stack)
            
        
