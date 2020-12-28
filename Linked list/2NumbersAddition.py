# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        sum1 = ""
        sum2 = ""
        while l1 or l2:
            if l1:
                sum1 = sum1 + str(l1.val)
                l1 = l1.next
            if l2:
                sum2 = sum2 + str(l2.val)
                l2 = l2.next

        sum3 = int(sum1[::-1]) + int(sum2[::-1])

        new = ListNode()
        aux = new
        k = 10
        while sum3 > 0 and aux:
            n = sum3 % k
            aux.val = n
            sum3 = sum3 // k

            if sum3 > 0:
                newNode = ListNode()
                aux.next = newNode
            aux = aux.next

        return new




