# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flat(self,root):
        if not root:
            return
        if root.left==None:
            self.flat(root.right)
        else:
            temp1 = root
            temp = root.right
            root.right = root.left
            root.left = None
            while(root.right!=None):
                root = root.right
            root.right = temp
            self.flat(temp1.right)
        return root
    def flatten(self, root):
        if not root:
            return 
        self.flat(root)
        return root