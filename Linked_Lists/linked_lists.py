# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ll_fast = head
        ll_slow = head
        count = 0
        while ll_fast:
            ll_fast = ll_fast.next
            if count %2 != 0:
                ll_slow = ll_slow.next
            count += 1

        return ll_slow