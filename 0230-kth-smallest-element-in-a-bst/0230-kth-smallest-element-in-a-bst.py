# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root):
        if not root:
            return
        self.preorder(root.left)
        self.ans.append(root.val)
        self.preorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = []
        self.preorder(root)
        return self.ans[k-1]
        