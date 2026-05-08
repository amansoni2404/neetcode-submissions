# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            head = None
            return head
        elif head is None:
            return head
        else:
            fast = slow = head
            pre = None
            while (n > 0):
                fast = fast.next
                n -= 1
            while fast is not None:
                pre = slow
                slow = slow.next
                fast = fast.next
            if pre:
                pre.next = slow.next
            else:
                head = slow.next
            slow.next = None
            return head
            
        