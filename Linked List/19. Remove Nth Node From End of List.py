from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC -> O(n)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.length(head) # O(n)
        count = 0
        prev = None
        cur = head

        # Go to the node that needs to be deleted
        while count < (length - n): # O(n)
            prev = cur
            cur = cur.next
            count += 1

        '''
            1. [] -> return []
            2. [1] -> return []
            3. [1,1] -> [1]
        '''
        if not prev:
            return cur.next
        else:
            prev.next = cur.next

        return head

    # TC -> O(n) where n is the length of LL
    def length(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        return 1 + self.length(head.next)
