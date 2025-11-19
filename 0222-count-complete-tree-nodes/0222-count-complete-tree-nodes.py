# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
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