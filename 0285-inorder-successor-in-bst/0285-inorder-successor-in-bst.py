# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root,p):
        if not root:
            return 
        if p.val<root.val:
            self.ans = root
            self.inorder(root.left,p)
        else:
            self.inorder(root.right,p)
    def inorderSuccessor(self, root, p):
        self.ans = 0 
        self.inorder(root,p)
        return self.ans