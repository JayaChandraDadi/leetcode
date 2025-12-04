# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def precedor(self,root):
        if root.left==None:
            return root.val
        root = root.left
        while(root.right):
            root = root.right
        return root.val
    def sucessor(self,root):
        if root.right==None:
            return root.val
        root = root.right
        while(root.left):
            root = root.left
        return root.val
    def delete(self,root,key):
        if not root:
            return 
        if key<root.val:
           root.left = self.delete(root.left,key)
        elif key>root.val:
            root.right = self.delete(root.right,key)
        else:
            if root.left==None and root.right==None:
                root=None
            elif root.left:
                root.val = self.precedor(root)
                root.left = self.delete(root.left,root.val)
            else:
                root.val = self.sucessor(root)
                root.right = self.delete(root.right,root.val)
        return root
    def deleteNode(self, root, key):
        return self.delete(root,key)
        