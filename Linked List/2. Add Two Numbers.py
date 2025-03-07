from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC - O(max(m,n)) where m -> len(l1) and n -> len(l2)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        temp = ans
        carry = 0

        while l1 or l2 or carry:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            summed_val = v1+v2+carry
            carry = summed_val // 10 if summed_val > 9 else 0
            temp.next = ListNode(summed_val % 10)
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans.next
