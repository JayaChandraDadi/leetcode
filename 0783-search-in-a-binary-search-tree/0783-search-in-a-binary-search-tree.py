# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return 
        node = root
        while(node!=None):
            if node.val==val:
                return node
            elif val<node.val:
                node = node.left
            else:
                node = node.right
        return 

