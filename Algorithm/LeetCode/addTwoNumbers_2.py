# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode.com/problems/add-two-numbers/
class Solution:

    def get_sc(self, x, y, c):
        sum_ = x + y + c
        return (sum_) % 10, int(sum_ / 10)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        head = l1
        carry = 0
        prev = l1
        oneList = False

        while (l1 != None or l2 != None):
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            sum = x + y + carry
            carry = int(sum / 10)
            l1.val = sum % 10

            if l1.next == None and l2 != None:
                l1.next = l2.next
                l2 = None

            prev = l1
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if carry != 0:
            prev.next = ListNode(carry)
        return head