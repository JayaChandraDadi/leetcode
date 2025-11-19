# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def count(self,root):
        if not root:
            return 0
        leftnodes = self.count(root.left)
        rightnodes = self.count(root.right)
        return 1+leftnodes+rightnodes
    def countNodes(self, root):
        if not root:
            return 0
        return self.count(root)
        queue = deque()
        ct = 0
        queue.append(root)
        while(queue):
            for i in range(len(queue)):
                temp = queue.popleft()
                ct+=1
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return ct