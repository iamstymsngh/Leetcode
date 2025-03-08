from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC -> O(NLogN)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        middle = self.middleNode(head)
        head2 = middle.next
        middle.next = None

        left = self.sortList(head)
        right = self.sortList(head2)

        return self.mergeTwoLists(left, right)

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow if slow else None

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1)
        dummy = new_head

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            else:
                dummy.next  = list2
                list2 = list2.next
                dummy = dummy.next

        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2

        return new_head.next
