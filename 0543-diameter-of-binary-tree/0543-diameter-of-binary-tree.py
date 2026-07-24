# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameter(self,root):
        if not root:
            return 0
        lh = self.diameter(root.left)
        rh = self.diameter(root.right)
        self.maxi = max(self.maxi,lh+rh)
        return 1+max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        self.diameter(root)
        return self.maxi

        