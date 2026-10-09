class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for i in range(len(s)):
            # s 负责增加计数，t 负责抵消扣减计数
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        return all(c == 0 for c in counts)

        