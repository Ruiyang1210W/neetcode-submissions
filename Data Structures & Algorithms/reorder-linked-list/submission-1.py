# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. 快慢指针找中点
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. 反转后半段链表（从 slow 开始反转，而不是从 head 开始！）
        prev, curr = None, slow
        while curr:
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_

        # 3. 缝合交错合并
        first, second = head, prev
        while second.next:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
