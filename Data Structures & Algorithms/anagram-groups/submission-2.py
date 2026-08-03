class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a-z

            for c in s:
                count[ord(c) - ord("a")] += 1 # 把字母变成 0 到 25 的数组下标

            res[tuple(count)].append(s) # Python 禁止用 list 当字典的 Key
        
        return list(res.values())