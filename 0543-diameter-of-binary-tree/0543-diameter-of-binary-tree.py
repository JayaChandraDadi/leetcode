# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        temp = root
        maxi = [0]
        def dfs(temp,maxi):
            if temp==None:
                return 0
            left = dfs(temp.left,maxi)
            right = dfs(temp.right,maxi)
            maxi[0] = max(left+right,maxi[0])
            return 1+max(left,right)
        dfs(temp,maxi)
        return maxi[0]
        