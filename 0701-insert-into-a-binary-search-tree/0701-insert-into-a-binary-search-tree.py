# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insert(self,root,val):
        if not root:
            node = TreeNode(val)
            return node
        if root.left==None and root.right==None:
            node = TreeNode(val)
            if root.val>node.val:
                root.left = node
            else:
                root.right = node
            return root
        if val<root.val:
            root.left = self.insert(root.left,val)
        if val>root.val:
            root.right = self.insert(root.right,val)
        return root
    def insertIntoBST(self, root, val):
        return self.insert(root,val)