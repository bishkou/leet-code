# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        first = headA
        second = headB
        i = 1
        j = 1

        while first or second:
            if first:
                first = first.next
                i += 1
            if second:
                second = second.next
                j += 1
        first = headA
        second = headB
        if i >= j:
            for k in range(i - j):
                first = first.next
            while first:
                if first == second:
                    return first
                first = first.next
                second = second.next

        else:
            for k in range(j - i):
                second = second.next
            while second:
                if first == second:
                    return first
                first = first.next
                second = second.next

        return None