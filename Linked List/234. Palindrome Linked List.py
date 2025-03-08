from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC -> O(n)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle_node = self.middleNode(head)
        head2 = middle_node.next
        middle_node.next = None
        rev_head = self.reverse(head2)
        while head and rev_head:
            if head.val != rev_head.val:
                return False
            head = head.next
            rev_head = rev_head.next
        return True

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