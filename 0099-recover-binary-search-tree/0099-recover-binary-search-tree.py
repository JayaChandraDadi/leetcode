# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        first = None
        second = None
        prev = None
        def dfs(root):
            nonlocal first,second,prev
            if not root:
                return 
            dfs(root.left)
            if prev and prev.val>root.val:
                if not first:
                    first = prev
                second = root
            prev = root
            dfs(root.right)
        dfs(root)
        first.val,second.val = second.val,first.val

        return root