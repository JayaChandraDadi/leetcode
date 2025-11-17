# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root==None:
            return []
        q = deque()
        q.append(root)
        ans = []
        while(q):
            level = []
            for i in range(len(q)):
                temp = q.popleft()
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            ans.append(level)
        return ans
                
