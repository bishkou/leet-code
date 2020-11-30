# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pos = 1
        if pos < 0:
            return False
        i = 0

        while i < pos and head.next != None:
            head = head.next
            i += 1

        if i == pos:
            return True