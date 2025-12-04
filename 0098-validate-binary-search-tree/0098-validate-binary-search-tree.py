# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def preorder(self,root,ans):
        if not root:
            return 
        self.preorder(root.left,ans)
        ans.append(root.val)
        self.preorder(root.right,ans)
        return ans
    def isValidBST(self, root):
        ans = self.preorder(root,[])
        for i in range(1,len(ans)):
            if ans[i-1]>=ans[i]:
                return False
        return True       