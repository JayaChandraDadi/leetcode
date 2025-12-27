# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.left)
        if root.val not in self.ans:
            self.ans[root.val] = 0
        self.ans[root.val]+=1
        self.inorder(root.right)
    def findMode(self, root):
        self.ans = {}
        self.inorder(root)
        max_freq = max(self.ans.values())
        res = []
        for key in self.ans:
            if max_freq==self.ans[key]:
                res.append(key)
        return res
        
        