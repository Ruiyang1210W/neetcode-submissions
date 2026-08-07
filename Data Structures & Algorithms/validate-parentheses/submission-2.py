class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'}':'{', ')':'(', ']':'['}
        for c in s:
            if c in hashmap:
                # 1. stack：先检查栈是不是【非空】（防止栈为空时访问 stack[-1] 引发 IndexError 崩溃）
                # 2. stack[-1] == hashmap[c]：查看【栈顶元素】（最近一个没被匹配的左括号），
                #    检查它是否刚好是当前右括号 c 所对应的【匹配左括号】
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        