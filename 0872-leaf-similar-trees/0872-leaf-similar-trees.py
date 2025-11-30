# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,root,ans):
        if root==None:
            return 
        if root.left==None and root.right==None:
            ans.append(root.val)
        self.check(root.left,ans)
        self.check(root.right,ans)
        return ans
    def leafSimilar(self, root1, root2):
        return self.check(root1,[])==self.check(root2,[])
        
        