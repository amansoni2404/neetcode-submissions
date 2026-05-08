# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast , slow = head, head
        if not head:
            return False
        if head.next == None:
            return False
        while fast is not None:
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if fast == slow:
                return True
        return False

        