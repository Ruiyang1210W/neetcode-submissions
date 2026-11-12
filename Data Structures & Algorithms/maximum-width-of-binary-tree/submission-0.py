# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        node_q = deque([root])
        pos_q = deque([0])
        max_width = 0

        while node_q:
            level_size = len(node_q)
            leftmost = pos_q[0]
            rightmost = pos_q[-1]
            max_width = max(max_width, rightmost - leftmost + 1)

            for _ in range(level_size):
                node = node_q.popleft()
                pos = pos_q.popleft() - leftmost

                if node.left:
                    node_q.append(node.left)
                    pos_q.append(2 * pos + 1)
                if node.right:
                    node_q.append(node.right)
                    pos_q.append(2 * pos + 2)

        return max_width
