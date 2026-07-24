# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def robbery(self,root):
        if not root:
            return (0,0)
        left = self.robbery(root.left)
        right = self.robbery(root.right)
        rob = root.val + left[1] + right[1]
        not_rob = max(left) + max(right)
        return [rob,not_rob]
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.robbery(root)
        return max(res)