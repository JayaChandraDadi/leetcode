# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         se lf.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findleftheight(self,node):
        ht = 0
        while(node!=None):
            ht+=1
            node = node.left
        return ht
    def findrightheight(self,node):
        ht = 0
        while(node!=None):
            ht+=1
            node = node.right
        return ht
    def countNodes(self, root):
        if root==None:
            return 0
        lh = self.findleftheight(root)
        rh = self.findrightheight(root)
        if lh==rh:
            return (1<<lh)-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        