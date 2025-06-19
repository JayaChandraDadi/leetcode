# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    first = None
    last = None
    prev = None
    middle = None
    def inorder(self,root):
        if root==None:
            return 
        self.inorder(root.left)
        if self.prev!=None and self.prev.val>root.val:
            if self.first==None:
                self.first = self.prev
                self.middle = root
            else:
                self.last = root
        self.prev = root
        self.inorder(root.right)
    def recoverTree(self, root):
        prev = TreeNode(float('-inf'))
        self.inorder(root)
        if self.first and self.last:
            self.first.val,self.last.val = self.last.val,self.first.val
        elif self.first and self.middle:
            self.first.val,self.middle.val = self.middle.val,self.first.val

        