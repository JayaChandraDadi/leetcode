# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if not root:
            return 
        self.dfs(root.left)
        self.inorder.append(root.val)
        self.dfs(root.right)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder = []
        minlen = float('inf')
        self.dfs(root)
        for i in range(1,len(self.inorder)):
            minlen = min(minlen,abs(self.inorder[i] - self.inorder[i-1]))
        return minlen