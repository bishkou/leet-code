# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        deep_copy_dict = {}
        if not head:
            return None
        current_node = head
        while current_node:
            deep_copy_dict[current_node] = Node(current_node.val, None, None)
            current_node = current_node.next
        current_node = head
        while current_node:
            if current_node.next:
                deep_copy_dict[current_node].next = deep_copy_dict.get(current_node.next)
            if current_node.random:
                deep_copy_dict[current_node].random = deep_copy_dict.get(current_node.random)
            current_node = current_node.next

        return deep_copy_dict.get(head)