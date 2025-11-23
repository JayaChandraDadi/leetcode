# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def verticalTraversal(self, root):
        queue = deque()
        queue.append([root,0,0])
        nodes = []
        while(queue):
            for i in range(len(queue)):
                node,row,col = queue.popleft()
                nodes.append([col,row,node.val])
                if node.left:
                    queue.append([node.left,row+1,col-1])
                if node.right:
                    queue.append([node.right,row+1,col+1])
        nodes.sort()
        res = []
        prev_col = float('-inf')
        for col,row,value in nodes:
            if col!=prev_col:
                res.append([])
                prev_col = col
            res[-1].append(value)
        return res