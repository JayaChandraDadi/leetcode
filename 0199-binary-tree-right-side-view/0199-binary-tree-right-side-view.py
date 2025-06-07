# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        self.ans = []
        def dfs(node,level):
            if node==None:
                return
            if level==len(self.ans):
                self.ans.append(node.val)
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        dfs(root,0)
        return self.ans
        