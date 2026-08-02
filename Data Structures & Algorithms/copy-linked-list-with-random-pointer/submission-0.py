"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None} # 哨兵：None 对应 None、

        # 建立“旧人到新人”的映射字典（HashMap）
        cur = head
        while cur:
            copy = Node(cur.val) # 1. 复制一个数值一模一样的新节点
            oldToCopy[cur] = copy # 2. 在字典里记录：原版节点 cur -> 副本节点 copy
            cur = cur.next


        # 第二轮扫描：查字典，连上线！
        cur = head
        while cur:
            copy = oldToCopy[cur] # 拿到当前的副本节点
            copy.next = oldToCopy[cur.next] # 👑 连接新节点的 next
            copy.random = oldToCopy[cur.random] # 👑 连接新节点的 random
            cur = cur.next
        
        return oldToCopy[head]