# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if fast:       
            while fast.next:
                fast = fast.next
                slow = slow.next
            nth = slow.next
            slow.next = nth.next
            nth.next = None
            return head
        else:
            head = slow.next
            return head
        