# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans = []
    def preorderTraversal(self, root):
        ans = []
        def preorder(self,temp):
            if temp == None:
                return 
            else:
                ans.append(temp.val)
                preorder(self,temp.left)
                preorder(self,temp.right)
        preorder(self,root)
        return ans

