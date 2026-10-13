# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_):
            if not node:
                return 0

            count = 1 if node.val >= max_ else 0

            curr_max = max(node.val, max_)

            left = dfs(node.left, curr_max)
            right = dfs(node.right, curr_max)

            return count + left + right

        return dfs(root, root.val)