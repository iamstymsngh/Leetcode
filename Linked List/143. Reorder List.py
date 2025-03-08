from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = self.middleNode(head)
        head2 = middle.next
        middle.next = None

        rev_head = self.reverse(head2)
        new_head = ListNode(-1)
        dummy = new_head
        while head and rev_head:
            dummy.next = head
            dummy = dummy.next
            head = head.next

            dummy.next = rev_head
            dummy = dummy.next
            rev_head = rev_head.next

        if head:
            dummy.next = head
            dummy = dummy.next
        if rev_head:
            dummy.next = rev_head
            rev_head = rev_head.next

        return new_head.next

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow if slow else None

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur, prev = head, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
