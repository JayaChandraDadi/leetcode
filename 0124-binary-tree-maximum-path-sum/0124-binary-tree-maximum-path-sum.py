# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxi = float('-inf')
        def dfs(node):
            if node==None:
                return 0
            leftsum = max(0,dfs(node.left))
            rightsum = max(0,dfs(node.right))
            self.maxi = max(self.maxi,leftsum+rightsum+node.val)
            return node.val + max(leftsum,rightsum)
        k = dfs(root)
        return self.maxi
        