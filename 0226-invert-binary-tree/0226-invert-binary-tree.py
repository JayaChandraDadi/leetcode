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
        temp = root.left
        root.left = root.right
        root.right = temp
        self.dfs(root.left)
        self.dfs(root.right)
        return root
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)