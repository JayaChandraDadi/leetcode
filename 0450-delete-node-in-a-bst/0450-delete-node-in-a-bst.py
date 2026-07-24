# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self,root):
        while(root and root.left):
            root = root.left
        return root
    def dfs(self,root,key):
        if not root:
            return None
        if key<root.val:
            root.left = self.dfs(root.left,key)
        elif key>root.val:
            root.right = self.dfs(root.right,key)
        else:
            new_key = self.successor(root.right)
            if new_key==None:
                return root.left
            root.val = new_key.val
            root.right = self.dfs(root.right,new_key.val)
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.dfs(root,key)