# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self,root):
        if not root:
            return
        self.preorder(root.left)
        self.k-=1
        if self.k==0:
            self.result = root.val
            return 
        self.preorder(root.right)
    def kthSmallest(self, root, k):
        self.k = k
        self.result = 0
        self.preorder(root)
        return self.result
        