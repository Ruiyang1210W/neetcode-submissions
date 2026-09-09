class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        length = 0
        if len(s) == 1:
            return 1
        
        for i in s:
            hashmap[i] = hashmap.get(i,0) + 1

            if hashmap[i] % 2 == 0:
                length += 2

        for i in hashmap.values():
            # 如果有任何字符落单（奇数次），可以在正中间放 1 个作为回文中心。
            if i % 2:
                # 等价于显式写出的: if i % 2 == 1: 或 if i % 2 != 0
                length += 1
                break
        
        return length