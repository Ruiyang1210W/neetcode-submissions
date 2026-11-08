# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            level_size = len(q)

            for i in range(level_size):
                curr = q.popleft()
                if i == level_size - 1:
                    result.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

        
        return result