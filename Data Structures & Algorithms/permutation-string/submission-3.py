class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 =len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        # 统计s1 和s2 前n1 个字符频次
        for i in range(n1):
            s1_count[ord(s1[i])- ord('a')] += 1
            s2_count[ord(s2[i])- ord('a')] += 1

        if s1_count == s2_count:
            return True

        # 维护一个长度固定为n1的滑动窗口
        for i in range(n1, n2):
            # 右边新进一个字符
            s2_count[ord(s2[i]) - ord('a')] += 1
            # 左边划出一个字符
            s2_count[ord(s2[i - n1]) - ord('a')] -= 1

            # 比较26个字母频次是否完全一致
            if s1_count == s2_count:
                return True
        
        return False
            