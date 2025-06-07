# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        queue= deque()
        if not root:
            return 0
        width = 0
        last = 0
        first = 0
        queue.append((root,0))
        while(len(queue)!=0):
            length = len(queue)
            mini = queue[0][1]
            for i in range(length):
                node,currid = queue.popleft()
                currid = currid-mini
                if i==0:
                    first = currid
                if i==length-1:
                    last = currid
                if node.left:
                    queue.append((node.left,2*currid+1))
                if node.right:
                    queue.append((node.right,2*currid+2))
            width = max(width,last-first+1)
        return width







