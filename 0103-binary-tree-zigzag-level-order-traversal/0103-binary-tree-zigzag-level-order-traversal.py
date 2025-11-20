# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = deque()
        flag = 0
        ans = []
        queue.append(root)
        while(queue):
            level = []
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                level.append(temp.val)
            if flag==0:
                ans.append(level)
                flag = 1
            else:
                ans.append(level[::-1])
                flag = 0
        return ans
