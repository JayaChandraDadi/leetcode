# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def build(self,bound,preorder):
        if self.i==len(preorder) or preorder[self.i]>bound:
            return None
        node = TreeNode(preorder[self.i])
        self.i+=1
        node.left = self.build(node.val,preorder)
        node.right = self.build(bound,preorder)
        return node
    def bstFromPreorder(self, preorder):
        self.i = 0
        return self.build(float('inf'),preorder)
        