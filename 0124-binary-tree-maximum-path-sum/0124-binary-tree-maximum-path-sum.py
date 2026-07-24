# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathsum(self,root):
        if not root:
            return 0
        leftsum = max(self.pathsum(root.left),0)
        rightsum = max(self.pathsum(root.right),0)
        self.maxi = max(self.maxi,leftsum+rightsum+root.val)
        return max(leftsum,rightsum) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
         self.maxi = float('-inf')
         self.pathsum(root)
         return self.maxi
        