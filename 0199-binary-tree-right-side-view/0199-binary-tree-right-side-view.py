# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightview(self,root,ans,level):
        if not root:
            return []
        if level==len(ans):
            ans.append(root.val)
        self.rightview(root.right,ans,level+1)
        self.rightview(root.left,ans,level+1)
        return ans
    def rightSideView(self, root):
        ans = []
        return self.rightview(root,ans,0)
        return ans
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while(queue):
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            ans.append(temp[-1])
        return ans
        