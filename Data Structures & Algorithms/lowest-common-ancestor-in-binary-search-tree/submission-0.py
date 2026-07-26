# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        # BST 左小右大
        while curr:
            # 两个人都在右边，往右找
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # 两个人都在左边，往左找
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # 两个人要分家了，或者其中一个人就是当前节点，当前节点就是最近公共祖先！
                return curr