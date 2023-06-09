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

#744. Find Smallest Letter Greater Than Target
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
#  There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does
#  not exist, return the first character in letters.
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letter_returned = letters[0]

        for letter in letters:
            if letter > target:
                letter_returned = letter
                break
        return letter_returned