class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1 # counts how many times each letter (a–z) appears in a word.
            res[tuple(count)].append(s)
        return list(res.values())
                

        
        