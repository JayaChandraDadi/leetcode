# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return False
        def symmetry(left,right):
            if left==None or right==None:
                return left==right
            if left.val!=right.val:
                return False
            return symmetry(left.left,right.right) and symmetry(left.right,right.left)
        return symmetry(root.left,root.right)
        
        