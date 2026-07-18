class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        target = sorted(s1)
        # 尺子长度是 len1，所以起点 i 最多只能走到 len2 - len1 的位置
        for i in range(len2 - len1 + 1):
            sub_str = s2[i: i+len1]
            if sorted(sub_str) == target:
                return True
            
        return False
    
       
