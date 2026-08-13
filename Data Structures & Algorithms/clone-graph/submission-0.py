"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        if not node:
            return None

        def dfs(node): # clone neighbors recursively
            if node in oldToNew: #already made a clone of it
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))
            return copy
        
        
        return dfs(node)