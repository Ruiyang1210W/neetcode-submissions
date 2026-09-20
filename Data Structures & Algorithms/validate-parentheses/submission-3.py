class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char in hashmap:
                if not stack or stack[-1] != hashmap[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0