# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # inital a dummy node
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # 让 right 先往前领跑 n 步，拉开距离
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # 两个指针保持距离，齐步走！直到 right 走到终点 None
        while right:
            left = left.next
            right = right.next
        
        # delete：此时 left 刚好停在【倒数第 n 个节点】
        left.next = left.next.next 

        return dummy.next
