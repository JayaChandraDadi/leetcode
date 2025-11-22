# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isleaf(self,root):
        if not root:
            return False
        if root.left==None and root.right==None:
            return True
        return False
    def leaves(self,root,ans):
        if not root:
            return 
        if self.isleaf(root):
            ans.append(root.val)
        self.leaves(root.left,ans)
        self.leaves(root.right,ans)
        return ans
    def leftboundary(self,root,ans):
        if not root:
            return 
        if self.isleaf(root):
            return 
        ans.append(root.val)
        if root.left:
            self.leftboundary(root.left,ans)
        else:
            self.leftboundary(root.right,ans)
        return ans
    def rightboundary(self,root,ans):
        if not root:
            return 
        if self.isleaf(root):
            return 
        ans.append(root.val)
        if root.right:
            self.rightboundary(root.right,ans)
        else:
            self.rightboundary(root.left,ans)
        return ans
    def boundaryOfBinaryTree(self, root):
        if self.isleaf(root):
            return [root.val]
        ans = []
        ans.append(root.val)
        self.leftboundary(root.left,ans)
        self.leaves(root,ans)
        rightans = []
        self.rightboundary(root.right,rightans)
        ans+=rightans[::-1]
        return ans