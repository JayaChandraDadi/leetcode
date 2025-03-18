"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
       hashmap = {}
       temp = head
       if head==None:
        return 
       while(temp!=None):
        newnode = Node(temp.val)
        hashmap[temp] = newnode
        temp = temp.next
       temp = head
       while(temp!=None):
        copynode = hashmap[temp]
        copynode.next = hashmap.get(temp.next)
        copynode.random = hashmap.get(temp.random)
        temp = temp.next
       return hashmap[head]

        