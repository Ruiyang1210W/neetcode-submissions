class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        result = 0
        left = 0
        right = 0
        end = len(s)
        while right < end:
            if s[right] not in hashmap:
                hashmap[s[right]] = 1
                right = right + 1
                result = max(result, right-left)
            else:
                del hashmap[s[left]]
                left = left + 1
            
        return result

