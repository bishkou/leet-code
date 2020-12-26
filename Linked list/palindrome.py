# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if head is None:
            return True

        tab = []

        while head:
            tab.append(head.val)
            head = head.next

        i = 0
        j = len(tab) - 1

        while i < j:
            if tab[i] != tab[j]:
                return False
            i += 1
            j -= 1

        return True

