# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left -> right -> root
        res = []

        def postorder(node):
            if not node:
                return  #在写任何递归（特别是二叉树 DFS）时，第一行永远要是这种保命门禁 Base Case
            
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)
        
        postorder(root)
        return res