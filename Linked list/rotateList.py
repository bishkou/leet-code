# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        if l == 0: return None
        k = k % l
        if k == 0: return head
        node = head
        counter = l - 1
        while node:
            if counter == k:
                mid_node = node
            if counter == 0:
                tail_node = node
            node = node.next
            counter -= 1

        new_nead = mid_node.next
        mid_node.next = None
        tail_node.next = head

        return new_nead