# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ct = 0
    def countgoodnodes(self,root,maxi):
        if not root:
            return 
        if root.val>=maxi:
            self.ct+=1
            maxi = root.val
        self.countgoodnodes(root.left,maxi)
        self.countgoodnodes(root.right,maxi)
    def goodNodes(self, root):
        maxi = root.val
        self.countgoodnodes(root,maxi)
        return self.ct