class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # defaultdix 自动初始化不存在的 Key，防止 KeyError 报错
        for s in strs:
            sortedS = ''.join(sorted(s)) # 2. 将字符串按字母排序，拼回字符串作为唯一 key
            ans[sortedS].append(s) # 3. 自动追加到对应 key 的列表中
        return list(ans.values())
        