# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            # ignore negative downward paths
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            max_sum = max(max_sum, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)


        dfs(root)
        return max_sum