# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)
    def swap(self,root,x,y):
        if not root:
            return 
        if root.val==x:
            root.val = y
        elif root.val==y:
            root.val = x
        self.swap(root.left,x,y)
        self.swap(root.right,x,y)
    def recoverTree(self, root):
        self.ans = []
        self.inorder(root)
        x=None
        y = None
        for i in range(1,len(self.ans)):
            if self.ans[i]<self.ans[i-1]:
                if x==None:
                    x = self.ans[i-1]
                y = self.ans[i]
        self.swap(root,x,y)
        return root