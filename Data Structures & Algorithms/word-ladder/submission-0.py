from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. 把词典转成 set，查询和删除都是 O(1)，同时充当 visited 集合！
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # 2. 标准 BFS 队列：存入 (当前单词, 当前步数)
        q = deque([(beginWord, 1)])

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            # 3. 找邻居：依次把单词的第 i 个位置替换成 'a' ~ 'z'
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue
                    next_word = word[:i] + ch + word[i+1:]

                    # 4. 如果新单词在词典里，入队并立刻从 set 中删掉（防走回头路）
                    if next_word in word_set:
                        word_set.remove(next_word)
                        q.append((next_word, steps + 1))

        return 0