# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)
    def minDiffInBST(self, root):
        min1 = float('inf')
        self.ans = []
        self.inorder(root)
        for i in range(1,len(self.ans)):
            min1 = min(min1,abs(self.ans[i]-self.ans[i-1]))
        return min1
        
        