"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # 第一步：DFS 收集所有节点的邻接关系 {val: [neighbor_vals]}
        adj = {}
        def dfs(curr):
            if curr.val in adj:
                return
            adj[curr.val] = [n.val for n in curr.neighbors]
            for neighbor in curr.neighbors:
                dfs(neighbor)

        dfs(node)

        # 第二步：根据收集好的 adj 字典，批量创建新 Node 并连接 neighbors
        clones = {val: Node(val) for val in adj}
        for val, neighbors in adj.items():
            clones[val].neighbors = [clones[n_val] for n_val in neighbors]

        return clones[node.val]
        