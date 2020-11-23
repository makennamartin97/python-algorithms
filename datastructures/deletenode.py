# leetcode: delete node in a linked list
# Write a function to delete a node in a singly-linked list. You will not be 
# given access to the head of the list, instead you will be given access to 
# the node to be deleted directly.

# It is guaranteed that the node to be deleted is not a tail node in the list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # set node to remove to the next nodes val
        node.val = node.next.val
        # remove the next node / set current node to point to the next next node
        node.next = node.next.next