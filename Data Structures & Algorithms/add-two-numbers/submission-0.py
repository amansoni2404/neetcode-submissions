# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = carry = actual_sum = 0
        num1 = l1
        num2 = l2
        prev = None
        while num1 or num2 or carry:
            if not num1 and not num2:
                sum = carry
            elif not num1:
                sum = num2.val + carry
            elif not num2:
                sum = num1.val + carry
            else:
                sum = num1.val + num2.val + carry
            carry = sum // 10
            if not num1 and not num2:
                carry = None
            sum = sum % 10
            new_node = ListNode(sum)
            if not prev:
                head = new_node
            else:
                prev.next = new_node
            prev = new_node
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
        return head
        