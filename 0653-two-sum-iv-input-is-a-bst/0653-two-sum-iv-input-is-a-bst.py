# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,root):
        if not root:
            return 
        self.check(root.left)
        self.ans.append(root.val)
        self.check(root.right)
    def findTarget(self, root, k):
        self.ans = []
        self.check(root)
        i = 0
        j = len(self.ans)-1
        while(i<j):
            sum1 = self.ans[i] + self.ans[j]
            if sum1>k:
                j-=1
            elif sum1<k:
                i+=1
            else:
                return True
        return False
        