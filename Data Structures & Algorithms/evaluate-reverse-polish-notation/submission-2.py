class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda b, a: b + a,
            "-": lambda b, a: b - a,
            "*": lambda b, a: b * a,
            "/": lambda b, a: int(b/a) 
        }

        for i in tokens:
            if i in operators:
                a = stack.pop()
                b = stack.pop()
                stack.append(operators[i](b,a))
            else:
                stack.append(int(i))
        
        return stack[0]


        