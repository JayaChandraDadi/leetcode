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
        flag = 0
        queue = deque()
        queue.append(root)
        ans = []
        while(len(queue)!=0):
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
                temp.append(node.val)
            if flag==0:
                flag = 1
                ans.append(temp)
            else:
                flag = 0 
                ans.append(temp[::-1])
        return ans



        