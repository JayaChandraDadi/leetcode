# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def merge(self,root1,root2):
        if root1 and root2:
            root1.val+=root2.val
        elif root1:
            return root1
        else:
            return root2
        root1.left = self.merge(root1.left,root2.left)
        root1.right = self.merge(root1.right,root2.right)
        return root1
    def mergeTrees(self, root1, root2):
        return self.merge(root1,root2)