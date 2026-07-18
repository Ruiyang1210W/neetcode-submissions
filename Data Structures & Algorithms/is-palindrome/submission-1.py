class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(c.lower() for c in s if c.isalnum()) #只保留小写字母
        left = 0
        right = len(clean_s) - 1

        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
            

            
        