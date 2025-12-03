# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def search(self,root,val):
        if not root:
            return 
        if val>root.val:
            return self.search(root.right,val)
        if val<root.val:
            return self.search(root.left,val)
        else:
            return root
        return
    def searchBST(self, root, val):
        return self.search(root,val)
        