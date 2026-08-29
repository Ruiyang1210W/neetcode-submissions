# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def dfs(node, depth):
            if not node:
                return None

            # 如果当前深度正好等于当前已收集到的层数，说明这是该层最右侧的第一个节点
            if depth == len(res):
                res.append(node.val)
            
            # 👑 关键：优先遍历右子树，再遍历左子树
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
      
        dfs(root,0)
        return res
