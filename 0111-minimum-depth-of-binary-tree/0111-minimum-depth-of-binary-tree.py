# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def mindepth(self,root):
        if root==None:
            return 0
        if not root.left:
            return 1+self.mindepth(root.right)
        elif not root.right:
            return 1+self.mindepth(root.left)
        return 1+min(self.mindepth(root.left),self.mindepth(root.right))
    def minDepth(self, root):
        if not root:
            return 0
        return self.mindepth(root)
        q = deque()
        depth = 0
        q.append(root)
        while(q):
            depth+=1
            for i in range(len(q)):
                temp = q.popleft()
                if not temp.left and not temp.right:
                    return depth
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        
        if not root:
            return 0
        
        