# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        node = root
        while(True):
            if val>=node.val:
                if node.right!=None:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left!=None:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
        return root
