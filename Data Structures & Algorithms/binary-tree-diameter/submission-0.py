# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
        
        
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # 当前节点的高度 = 1（自己这一层） + 左右子树里更高的那一边的深度
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

        # O(n^2)

        
        