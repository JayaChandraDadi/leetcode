# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        q = deque()
        q.append([root,1])
        maxwidth = 0
        while(q):
            length = len(q)
            for i in range(len(q)):
                node,index = q.popleft()
                if i==0:
                    firstindex = index
                if i==length-1:
                    lastindex = index
                if node.left:
                    q.append([node.left,2*index+1])
                if node.right:
                    q.append([node.right,2*index+2])
            maxwidth = max(maxwidth,lastindex-firstindex+1)
        return maxwidth
        