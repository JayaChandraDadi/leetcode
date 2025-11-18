# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self,ans,root):
        if root==None:
            return ans
        self.preorder(ans,root.left)
        self.preorder(ans,root.right)
        ans.append(root.val)
        return ans
    def postorderTraversal(self, root):
        ans = []
        return self.preorder(ans,root)
        
        